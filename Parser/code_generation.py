import type_classes as tc
# import ast_transform
import node_classes as nc


class symbolTable:

    def __init__(self):
        self.symbol_table = [[]]
        self.temp_stack = []
        self.scope_stack = [
            0
        ]  # because we can get the levels of scope -> that is the enclosing function or scope

    def get_scope(self):
        return len(self.scope_stack) - 1

    def inc_scope(self):
        self.scope_stack.append(self.get_scope() + 1)
        self.symbol_table.append([])

    def dec_scope(self):
        self.scope_stack.pop()
        self.symbol_table.pop()

    def lookup(self, lexeme):
        for i in range(self.get_scope(), -1, -1):
            for record in self.symbol_table[i]:
                if record["lexeme"] == lexeme:
                    return record
        return None

    def lookup_cur_scope(self, lexeme):
        for record in self.symbol_table[self.get_scope()]:
            if record["lexeme"] == lexeme:
                return record
        return None

    def insert(self, record):
        self.symbol_table[self.get_scope()].append(record)

    def get_enclosing_fun(self, level=1):
        # reference : https://github.com/Hyper5phere/simple-c-compiler/blob/master/modules/scanner.py
        # TODO check the logic, major diff
        try:
            # for i in range(self.get_scope(), -1, -1):
            #     for record in self.symbol_table[i]:
            #         print(record)
            req_scope = self.symbol_table[self.scope_stack[-level] - 2]
            record = req_scope[-1]  # if we are return a value then we are in a function
            if record["type"] == "function":
                return record
            
            else:  # in the case let's say we are in a if block or loop block
                return self.get_enclosing_fun(level + 1)
            
        except IndexError:
            return None

class NodeVisitor:

    def visit(self, node):
        method = "visit_" + node.__class__.__name__
        # print(method)
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception("No visit_{} method".format(type(node).__name__))
    
class codeGenerator(NodeVisitor):
    
    def __init__(self):
        self.symtab = symbolTable()
        self.present_mem_ptr = 0

    def visit_Start(self, node):
        
        print(''' (module
                    ;; Memory with 1 page (64KB)
                    (memory (export "memory") 1)

                    (func (export "store_value_at_address") (param $value i32) (param $address i32)
                        ;; Store the value at the specified address in memory
                        (i32.store (local.get $address) (local.get $value))
                    )
              
                    (func $loadValueFromMemory (param $address i32) (result i32)
                        (i32.load
                        (local.get $address)  ;; Load value from specified address
                        )
                    )
              
                    (func $arrindexing (param $index i32) (param $address i32) (result i32)
                        (local.get $index)   ;; Load the index parameter onto the stack
                        (i32.const 4)        ;; Load the constant value 4 onto the stack
                        (i32.mul)            ;; Multiply index by 4
        
                        ;; Add the address
                        (local.get $address) ;; Load the address parameter onto the stack
                        (i32.add)   
                    )
              
                    (func $logical_or (param $a i32) (param $b i32) (result i32)
                        ;; Perform bitwise OR
                        local.get $a
                        local.get $b
                        i32.or
                        ;; Convert result to 1 if non-zero (truthy), 0 otherwise (falsy)
                        i32.const 0
                        i32.ne
                        i32.const 1
                        select
                    )
              
                    (func $logical_not (param $a i32) (result i32)
                        ;; Convert $a to 0 or 1 (0 if $a is zero, 1 otherwise)
                        local.get $a
                        i32.const 0
                        i32.eq
                        i32.const 1
                        select
                    )
              
                    (func $logical_and (param $a i32) (param $b i32) (result i32)
                        ;; Perform bitwise AND
                        local.get $a
                        local.get $b
                        i32.and
                        ;; Convert result to 0 or 1 (0 if result is zero, 1 otherwise)
                        i32.const 0
                        i32.eq
                        i32.const 1
                        select
                    )
        ''')

        self.visit(node.children[0])
        print(")")

    def visit_Program(self, node):
        self.visit(node.children[0])

    def visit_Statements(self, node):
        for child in node.children:
            self.visit(child)

    def visit_NumberNode(self, node):

        number = node.val 
        print(f"i32.const {number}")
        print('\n')

    def visit_BitwiseExpr(self, node):

        left = self.visit(node.children[0])
        right = self.visit(node.children[2])
        op = node.children[1].value 

        if(op == '|'): print(f"i32.or")
        else: print(f"i32.and")

        print('\n')

    def visit_EqExpr(self, node):

        left = self.visit(node.children[0])
        right = self.visit(node.children[2])
        op = node.children[1].value 

        if(op == '=='): print(f"i32.eq")
        else: print(f"i32.ne")

        print('\n')

    def visit_CharNode(self, node):

        alph = node.val - 97
        print(f"i32.const {alph}")

        print('\n')


    def visit_AddExpr(self, node):

        left = self.visit(node.children[0])
        right = self.visit(node.children[2])
        op = node.children[1].value 

        if(op == '+'): print(f"i32.add")
        else: print(f"i32.sub")

        print('\n')

    def visit_MultExpr(self, node):
        
        left = self.visit(node.children[0])
        right = self.visit(node.children[2])
        op = node.children[1].value 

        if(op == '*'): print(f"i32.mul")
        elif(op == '%'): print(f"i32.rem_s")
        else: print(f"i32.div_s")

        print('\n')

  

    # def visit_PowerExpr(self, node):

    #     left = self.visit(node.children[0])
    #     right = self.visit(node.children[2])
    #     op = node.children[1].val 

    #     print(f"i32.mul")
        
    def visit_ExpressionStatement(self, node):
        self.visit(node.children[0])

    def visit_VariableDeclarationStatement(self, node):
        self.visit(node.children[0])

    def visit_VariableDeclaration(self, node):

        present_func = self.symtab.get_enclosing_fun()

        if present_func is None:
            record = {
                "lexeme": node.children[2].val,
                "type": "variable",
                "address": self.present_mem_ptr
            }
            
            self.symtab.insert(record)
            if len(node.children) == 5:
                self.visit(node.children[4])
            print(f"i32.const {self.present_mem_ptr}")
            print("(call $store_value_at_address)")
            self.present_mem_ptr += 4 

        else: 

            print(f"local ${node.children[2].val}")
            self.visit(node.children[4])
            print(f"local.set ${node.children[2].val} ")

        print('\n')

    def visit_VarNode(self, node):

        present_func = self.symtab.get_enclosing_fun()

        if present_func is None:
            record = self.symtab.lookup(node.val)
            address = record["address"]

            print(f"i32.const {address}")
            print("(call $loadValueFromMemory)")
        
        else:
            print(f"local.get ${node.val}") 

        print('\n')

    def visit_VariableChangeStatement(self, node):
        self.visit(node.children[0])

    def visit_VariableChange(self, node):

        present_func = self.symtab.get_enclosing_fun()
        record_andar = self.symtab.lookup_cur_scope(node.children[0].val) 
        
        if(present_func is not None and record_andar is not None):
            self.visit(node.children[-1])
            print(f"local.set {node.children[0].val}")

        else:
         
            self.visit(node.children[-1])
            if isinstance(node.children[0],nc.VarNode):
                record = self.symtab.lookup(node.children[0].val)
                address = record['address']
                print(f"i32.const {address}")
            elif isinstance(node.children[0],nc.Indexing):
                self.visit_IndexingAddress(node.children[0])

            print("(call $store_value_at_address)")
            print('\n')

    def visit_ConditionalStatement(self, node):

        self.visit(node.children[0].children[1]) # condition
        print("i32.const 1")
        print("i32.eq")

        print("(if(")
        print("then(")
        self.visit(node.children[0]) # if
        print(")")
        print("(else")
        self.visit(node.children[1]) # else
        print(")")
        print(")")
        print(")")
        print('\n')

    def visit_IfStatement(self, node):

        self.symtab.inc_scope()
        self.visit(node.children[2])  # statements
        self.symtab.dec_scope()

    def visit_ElseStatement(self, node):

        self.symtab.inc_scope()
        self.visit(node.children[1])  # statements
        self.symtab.dec_scope()

    def visit_OrCondition(self, node):

        self.visit(node.children[0])
        self.visit(node.children[2])
        
        print("(call $logical_or)")
        print('\n')

    def visit_AndCondition(self, node):
        self.visit(node.children[0])
        self.visit(node.children[2])
        
        print("(call $logical_and)")
        print('\n')

    def visit_NotCondition(self, node):
        self.visit(node.children[1])
        print("(call $logical_not)")
        print('\n')

    def visit_CompCondition(self, node):

        self.visit(node.children[0])
        self.visit(node.children[2]) 

        if(node.children[1].value == '<'): print("i32.lt_s")
        elif(node.children[1].value == '<='): print("i32.le_s")
        elif(node.children[1].value == '>='): print("i32.ge_s")
        else: print("i32.gt_s")

        print('\n')

    def visit_LoopStatement(self, node):
        
        self.symtab.inc_scope()
        if node.children[0].value == "for":
        
            # record = {
            #     "lexeme": node.children[1].children[2].val,
            #     "type": "variable",
            #     "address": self.present_mem_ptr
            # }

            # self.symtab.insert(record)
            self.visit(node.children[1])

            print("(loop $apnaloop")

            self.visit(node.children[2]) # condition
            print("i32.const 1")
            print("i32.eq")
            print("(if")
            print("(then")
            self.visit(node.children[-1]) # statements
            self.visit(node.children[-2]) # iteration
            print("br $apnaloop")
            print(")")
            print(")")
            print(")")
            
        else:
            print("(loop $apnaloop")
            self.visit(node.children[1]) # condition
            print("i32.const 1")
            print("i32.eq")

            print("(if")
            print("(then")
            self.visit(node.children[2])
            print("br $apnaloop")
            print(")")
            print(")")
            print(")")
            
        self.symtab.dec_scope()
        print('\n')
    
    def visit_lenNode(self, node):
        record = self.symtab.lookup(node.children[1].val)
        print(f"i32.const {record['length']}")
    
    def visit_Iteration(self, node):

        # print(self.symtab)
        # print(node.children[0].val)
        record = self.symtab.lookup(node.children[0].val)
        address = record['address']
        print(f"i32.const {address}")
        print("(call $loadValueFromMemory)")

        print("i32.const 1")
        if(node.children[1] == '--'): print("i32.sub")
        else: print("i32.add")

        print(f"i32.const {address}")
        print("(call $store_value_at_address)")
        print('\n')

    def visit_ArrayDeclaration(self,node):

        record = {
            "lexeme": node.children[1].val,
            "type": "array",
            "address": self.present_mem_ptr,
            "length" : 0
        }
        self.symtab.insert(record)
        if len(node.children) == 3:
            # value = node.children[2].val
            if isinstance(node.children[2], nc.NumberNode):
                value = node.children[2].val
                record["length"] = value
                # print(value)
            else:
                raise Exception("Array size should be a fixed number")
            for i in range(int(value)):
                print(f"i32.const {0}")
                print(f"i32.const {self.present_mem_ptr}")
                print("(call $store_value_at_address)")
                self.present_mem_ptr += 4
        elif len(node.children) == 4:

            if isinstance(node.children[2],nc.NumberNode):
                value = node.children[2].val
                record["length"] = value
                for i in range(int(value)):
                    self.visit(node.children[3])
                    print(f"i32.const {self.present_mem_ptr}")
                    print("(call $store_value_at_address)")
                    self.present_mem_ptr += 4
                
            elif isinstance(node.children[2],nc.VarNode):
                raise Exception("Array size should be a fixed number")
            else:
                record["length"] = len(node.children) - 3
                for i in range(3,len(node.children)):
                    self.visit(node.children[i])
                    print(f"i32.const {self.present_mem_ptr}")
                    print("(call $store_value_at_address)")
                    self.present_mem_ptr += 4
        else:
            record["length"] = len(node.children) - 3
            for i in range(3,len(node.children)):
                self.visit(node.children[i])
                print(f"i32.const {self.present_mem_ptr}")
                print("(call $store_value_at_address)")
                self.present_mem_ptr += 4
    
    def visit_IndexingAddress(self, node):

        record = self.symtab.lookup(node.children[0].val)
        address = record['address']
        self.visit(node.children[1])
        print(f"i32.const {address}")
        print("(call $arrindexing)")
    
    def visit_Indexing(self, node):
    
        self.visit_IndexingAddress(node)
        print("(call $loadValueFromMemory)")

    
    def visit_FunctionDeclaration(self, node):
        #! we need to add the parameters types in to the next scope
        record = {
            "lexeme": node.children[1].val,
            "type": "function",
        }

        temp_list = []
        final_str  = f"(func ${node.children[1].val}"

        # print("datatype",record['lexeme'], record['return_type'])
        # Implement the case for arrays and tuples also
        for node_ in node.children[2:-2]:
            if isinstance(node_, nc.VarNode):
                record2 = {
                    "lexeme": node_.val,
                    "type": "variable",
                    "address": self.present_mem_ptr
                }

                final_str += f"(param ${node_.val} i32)"

                # if isinstance(record["params"][-1], tc.Array) or isinstance(record["params"][-1], tc.Tuple):
                #     record2["object"] = record["params"][-1]
                #     record2["datatype"] = record["params"][-1].datatype

                # self.present_mem_ptr += 4
                temp_list.append(record2)
                continue
        
        record["params"] = temp_list 
        self.symtab.insert(record)
        self.symtab.inc_scope()
        for record in temp_list:
            self.symtab.insert(record)
        
        final_str += "(result i32)"
        print(final_str)
        self.visit(node.children[-1])
        self.symtab.dec_scope()
        print(")")
        print(f'''(export "{node.children[1].val}" (func ${node.children[1].val}))''')
        print('\n')

    def visit_FunctionCall(self, node):
        
        record = self.symtab.lookup(node.children[0].val)
        self.visit(node.children[1])
        print(f"(call ${record['lexeme']})")
        print('\n')

    def visit_ParametersCall(self, node):
        for child in node.children:
            self.visit(child)

    def visit_ReturnStatement(self, node):

        # this where levels will be imp -> check the return type
        # TODO we need to also handle closures
        self.visit(node.children[1])
        print('\n')

    





    

        



        

        

        

       

        

    