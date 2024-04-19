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
            req_scope = self.symbol_table[self.scope_stack[-level] - 1]
            record = req_scope[-1]  # if we are return a value then we are in a function
            # print(req_scope)
            if record["type"] == "function":
                return record
            else:  # in the case let's say we are in a if block or loop block
                return self.get_enclosing_fun(level + 1)
        except IndexError:
            return None


class NodeVisitor:

    def visit(self, node):
        method = "visit_" + node.__class__.__name__
        print(method)
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception("No visit_{} method".format(type(node).__name__))


class semanticCheck(NodeVisitor):

    def __init__(self):
        self.symtab = symbolTable()

    def visit_Start(self, node):
        self.visit(node.children[0])

    def visit_Program(self, node):
        self.visit(node.children[0])

    def visit_Statements(self, node):
        for child in node.children:
            self.visit(child)

    def visit_NumberNode(self, node):
        return tc.Number()

    def visit_FunctionDeclaration(self, node):
        #! we need to add the parameters types in to the next scope
        record = {
            "lexeme": node.children[1].val,
            "type": "function",
            "object": tc.Function_object(node.children[1].val),
            "return_type": self.get_datatype_(node.children[-2]),
            "params": [],
        }
        temp_list = []
        # print("datatype",record['lexeme'], record['return_type'])
        # Implement the case for arrays and tuples also
        for node_ in node.children[2:-2]:
            if isinstance(node_, nc.VarNode):
                record2 = {
                    "lexeme": node_.val,
                    "type": "variable",
                    "datatype": record["params"][-1],
                }
                if isinstance(record["params"][-1], tc.Array) or isinstance(record["params"][-1], tc.Tuple):
                    record2["object"] = record["params"][-1]
                    record2["datatype"] = record["params"][-1].datatype

                temp_list.append(record2)
                continue
            record["params"].append(self.get_datatype_(node_))

        if record["lexeme"] == "main":
            temp_record = self.symtab.lookup(record["lexeme"])
            if temp_record is not None:
                raise Exception("Main function already declared")

        else:
            temp_record = self.symtab.lookup_cur_scope(record["lexeme"])
            if temp_record is not None:
                raise Exception("Function already declared")

        self.symtab.insert(record)
        self.symtab.inc_scope()
        for record in temp_list:
            self.symtab.insert(record)
        self.visit(node.children[-1])
        self.symtab.dec_scope()
        return tc.Function_object(record["lexeme"])
    
    def visit_VariableDeclarationStatement(self, node):
        self.visit(node.children[0])

    def visit_VariableDeclaration(self, node):
        # print("HII")  
        record = self.symtab.lookup_cur_scope(node.children[2].val)
        # print(node.children[2].val)
        if record is not None:
            raise Exception("Variable already declared")

        record = {
            "lexeme": node.children[2].val,
            "type": "variable",
            "datatype": self.get_datatype_(
                node.children[1]
            ),  #! need a way to get the datatype from a token -> also consider the case of variables
        }
        # print(record,len(node.children))
        self.symtab.insert(record)
        if len(node.children) == 5:
          right = self.visit(node.children[4])
          # print(right, record["datatype"])
          if not isinstance(right, record["datatype"]):
              raise Exception(
                  "Type mismatch in variable declaration of ", record["lexeme"]
              )

        return None

    def visit_ArrayNode(self, node):
        return tc.Array(self.get_datatype_(node.children[1]))
    
    def visit_TupNode(self, node):
        return tc.Tuple(self.get_datatype_(node.children[1]))
    
    def visit_VariableChangeStatement(self, node):
        self.visit(node.children[0])

    def visit_Iteration(self, node):
        left = self.visit(node.children[0])
        if not isinstance(left, tc.Number):
            return ("Not a number") 
    
    def visit_VariableChange(self, node):
        left = self.visit(node.children[0])
        right = self.visit(node.children[-1])
        
        if isinstance(left,tc.Array) and isinstance(right,tc.Array):
            # print(left.datatype,right.datatype)
            
            if left.datatype != right.datatype:
                raise Exception("Type mismatch in variable change statement")
        elif isinstance(left,tc.Tuple) and isinstance(right,tc.Tuple):
            if left.datatype != right.datatype:
                raise Exception("Type mismatch in variable change statement")
        elif type(left) != type(right) or (
            not isinstance(left, tc.Datatype) or not isinstance(right, tc.Datatype)
        ):
            raise Exception("Type mismatch in variable change statement")
        return None

    def visit_Indexing(self, node):
        record = self.symtab.lookup(node.children[0].val)
        if record is None:
            raise Exception(
                "Variable ", record["lexeme"], " not declared before indexing"
            )
        if not isinstance(self.visit(node.children[1]),tc.Number):
            raise Exception("Index should be an integer")
        return record["datatype"]()

    def visit_ArrayDeclaration(self, node):
        #! Not included, the initialization of the array size and elements
        record = self.symtab.lookup_cur_scope(node.children[1].val)
        if record is not None:
            raise Exception("Variable Name already declared", node.children[1].val)
        record = {
            "lexeme": node.children[1].val,
            "type": "array_variable",
            "object": self.visit(node.children[0]),
            "datatype": self.visit(node.children[0]).datatype,
        }
        self.symtab.insert(record)
        if len(node.children) == 3:
            if self.get_datatype_(node.children[2]) != tc.Number:
                raise Exception("Array size should be an integer")
        elif len(node.children) == 4:
            if node.children[2].__class__.__name__ == "Token":
                for child in node.children[3:]:
                    child_type = self.visit(
                        child
                    )  #! need a way to get the datatype from a token
                    # print(child_type, record['object'].datatype)
                    if not isinstance(child_type, record["object"].datatype):
                        raise Exception(
                            "Type mismatch in array declaration of ", record["lexeme"]
                        )
            else:
                if self.get_datatype_(node.children[2]) != tc.Number:
                    raise Exception("Array size should be an integer")
                if self.get_datatype_(node.children[3]) != record["object"].datatype:
                    raise Exception(
                        "Type mismatch in array declaration of ", record["lexeme"]
                    )
        return None

    def visit_StringNode(self, node):
        return tc.String()

    def visit_TupleDeclaration(self, node):
        #! Not included, the initialization of the array size and elements
        record = self.symtab.lookup_cur_scope(node.children[1].val)
        if record is not None:
            raise Exception("Tuple already declared")
        record = {
            "lexeme": node.children[1].val,
            "type": "tuple_variable",
            "object": self.visit(node.children[0]),
            "datatype": self.visit(node.children[0]).datatype,
        }

        self.symtab.insert(record)
        for child in node.children[3:]:  #! need a way to get the datatype from a token
            child_type = self.visit(child)
            if not isinstance(child_type, record["object"].datatype):
                raise Exception(
                    "Type mismatch in tuple declaration of ", record["lexeme"]
                )

        return None

    def visit_FunctionCall(self, node):
        
        record = self.symtab.lookup(node.children[0].val)
        # print(record is None)
        if record is None:
            # raise Exception("Function ", node.children[0].val, " not declared before call")
            raise Exception(f"Function {node.children[0].val.value} not declared before call")
        if record["type"] != "function":
            raise Exception(record["lexeme"], " is not declared as a function before call")

        param_types = self.visit(node.children[1])
        param_types_f = record["params"]

        if len(param_types) != len(param_types_f):
            raise Exception(
                "Number of parameters in the call does not coincide with the number of parameters in the declaraton"
            )

        for i in range(len(param_types)):
            if param_types[i] != param_types_f[i] and type(param_types) != type(param_types_f):
                # print(param_types[i], param_types_f[i])
                raise Exception("Type mismatch in parameter {}".format(i + 1))
            
        if isinstance(record["return_type"],tc.Array) or isinstance(record["return_type"],tc.Tuple):
            return record["return_type"]
        return record["return_type"]()

    def visit_ConditionalStatement(self, node):
        for child in node.children:
            self.visit(child)

        return None

    def visit_IfStatement(self, node):

        self.symtab.inc_scope()
        first = self.visit(node.children[1])  # condition
        if not isinstance(first, tc.Bool):
            raise Exception("Operand inside if does not evaluate to a boolean")
        self.visit(node.children[2])  # statements
        self.symtab.dec_scope()

        return None

    def visit_ElseStatement(self, node):
        self.symtab.inc_scope()
        self.visit(node.children[1])  # statements
        self.symtab.dec_scope()

        return None

    def visit_VarNode(self, node):
        record = self.symtab.lookup(node.val)
        if record is None:
            raise Exception(f"Variable {node.val} referenced before assignment")
        # print(record)
        if "object" in record:
            return record["object"]
        else:
            return record["datatype"]()

    def get_datatype_(self, node):

        if isinstance(node, nc.NumberNode):
            return tc.Number

        elif isinstance(node, nc.StringNode):
            return tc.String

        elif isinstance(node, nc.CharNode):
            return tc.Char

        elif isinstance(node, nc.BoolNode):
            return tc.Bool

        elif isinstance(node, nc.VoidNode):
            return tc.Void
        elif isinstance(node, nc.ArrayNode):
            return tc.Array(self.get_datatype_(node.children[1]))

        record = self.symtab.lookup(node.val)
        if record is None:
            raise Exception(f"Variable {node.val} referenced before assignment")
        return record["datatype"]

    def visit_LoopStatement(self, node):
        # print("atleast here ", node.children[0].value)
        if node.children[0].value == "for":
            # print("here")
            # for i in range(len(node.children)):
            #     print(node.children[i])
            #     # print(node.children[i].value)
            # print("till here")
            
            self.symtab.inc_scope()
            # record = {
            #     "lexeme": node.children[3].children[0].val,
            #     "type": "variable",
            #     "datatype": self.get_datatype_(
            #         node.children[1].children[1]
            #     ),  #! need a way to get the datatype from a token -> also consider the case of variables
            # }

            self.visit(node.children[1])
            cond = self.visit(node.children[2])
            if not isinstance(cond, tc.Bool):
                # print(cond)
                # print(node.children[7])
                raise Exception("Inner operand does not evaluate to a boolean")

            # self.symtab.insert(record)
            self.visit(node.children[-2])
            self.visit(node.children[-1])
            self.symtab.dec_scope()

        else:

            cond = self.visit(node.children[1])
            if not isinstance(cond, tc.Bool):
                raise Exception("Inner operand does not evaluate to a boolean")

            self.visit(node.children[2])

        return None

    def visit_OrCondition(self, node):
        left = self.visit(node.children[0])
        right = self.visit(node.children[2])

        if (not isinstance(left, tc.Bool)) or (
            not isinstance(right, tc.Bool)
        ):  #! need to update based on the return type
            raise Exception("Type mismatch in AND condition")

        return tc.Bool()

    def visit_AndCondition(self, node):
        left = self.visit(node.children[0])
        right = self.visit(node.children[2])

        if (not isinstance(left, tc.Bool)) or (
            not isinstance(right, tc.Bool)
        ):  #! need to update based on the return type
            raise Exception("Type mismatch in AND condition")

        return tc.Bool()

    def visit_NotCondition(self, node):
        child = self.visit(node.children[1])
        if (
            not isinstance(child, tc.Bool)
        ):  #! need to update based on the return type
            raise Exception("Type mismatch in NOT condition")

        return tc.Bool()
        # what to return in this
    

    def visit_BitwiseExpr(self, node):
        left = self.visit(node.children[0])
        right = self.visit(node.children[2])
        # TODO need to see what types are allorwed -> This todo not done yet
        if (not isinstance(left, tc.Number)) or (
            not isinstance(right, tc.Number)
        ):  #! need to update based on the return type
            raise Exception("Type mismatch in Bitwise expression")
        return tc.Number()
    

    def visit_EqExpr(self, node):
        left = self.visit(node.children[0])
        right = self.visit(node.children[2])
        # TODO need to see what types are allorwed
        # TODO need to see what operations are allowed between bool and number ->
        # could allow all of them and return tc.Number(). To make things simple,
        # can just prohibit bool from most operations, which is not an unreasonable assumption
        cond = (type(left) == type(right)) and (isinstance(left, tc.Datatype))
        if not cond:  #! need to update based on the return type
            raise Exception("Type mismatch in Equality expression")

        return tc.Bool()
         # Since going to be used in an expression context; going to take the values 0 and 1

    def visit_CharNode(self, node):
        return tc.Char()

    def visit_ShiftExpr(self, node):
        left = self.visit(node.children[0])
        right = self.visit(node.children[2])
        # TODO need to see what types are allowed - only numbers
        if (not isinstance(left, tc.Number)) or (
            not isinstance(right, tc.Number)
        ):  #! need to update based on the return type
            raise Exception("Type mismatch in Shift expression")

        return tc.Number()

    def visit_AddExpr(self, node):

        left = self.visit(node.children[0])
        right = self.visit(node.children[2])
        # TODO need to see what types are allowed - numbers, string, char
        cond = (type(left) == type(right) or (isinstance(left,tc.String)and isinstance(right,tc.Char) )or(isinstance(left,tc.Char)and isinstance(right,tc.String))) and (
            isinstance(left, tc.Number)
            or isinstance(left, tc.String)
            or isinstance(left, tc.Char)
        )
        if not cond:  #! need to update based on the return type
            raise Exception("Type mismatch in Addition expression")

        if isinstance(left, tc.Number):
            return tc.Number()

        if isinstance(left, tc.String):
            return tc.String()

        return tc.Char()

    def visit_MultExpr(self, node):
        left = self.visit(node.children[0])
        right = self.visit(node.children[2])
        # TODO need to see what types are allowed - Only numbers
        if (not isinstance(left, tc.Number)) or (
            not isinstance(right, tc.Number)
        ):  #! need to update based on the return type
            raise Exception("Type mismatch in Multiplication expression")

        return tc.Number()

    def visit_PowerExpr(self, node):
        left = self.visit(node.children[0])
        right = self.visit(node.children[2])
        # TODO need to see what types are allowed  - Only numbers
        if (not isinstance(left, tc.Number)) or (
            not isinstance(right, tc.Number)
        ):  #! need to update based on the return type
            raise Exception("Type mismatch in Power expression")

        return tc.Number()
    
    def visit_VarInit(self, node):

        for child in node.children:
            self.visit(child)

        return None 

    # what is this function
    def visit_ParametersCall(self, node):
        # TODO
        result = []
        for child in node.children:

            if isinstance(child, nc.VarNode):
                record = self.symtab.lookup(child.val)
                # print(record)
                if record is None:
                    raise Exception("Variable referenced before assignment")

                if('object' in record): result.append(tc.Array(record["datatype"]))
                else: result.append(record["datatype"])

            elif isinstance(child, nc.NumberNode):
                result.append(tc.Number)

            elif isinstance(child, nc.StringNode):
                result.append(tc.String)

            elif isinstance(child, nc.BoolNode):
                result.append(tc.Bool)

            elif isinstance(child, nc.CharNode):
                result.append(tc.Char)

            elif isinstance(child, nc.ArrayNode):
                result.append(tc.Array(self.get_datatype_(child.children[1])))

        return result

    def visit_PrintStatement(self, node):
        # TODO we can have two ways -> we allow both int and string or we allow only one type -> Let's allow both
        # one thing we need to take care of is that in this complex val child -> format func -> Need to handle while visiting ComplexVal
        child = self.visit(node.children[1])
        if not isinstance(child, tc.Number) and not isinstance(child, tc.String):
            raise Exception("Type mismatch in Print statement")

        return None

    def visit_ExceptionHandling(self, node):
        pass

    def visit_ExpressionStatement(self, node):
        self.visit(node.children[0])
        return None

    def visit_ReturnStatement(self, node):
        # this where levels will be imp -> check the return type
        # TODO we need to also handle closures
        record = self.symtab.get_enclosing_fun()
        if record is None:
            raise Exception("Return statement outside function")
        # TODO modify the logic how to get the return type, through the record or through the object
        if record["return_type"] == tc.Void:
            if len(node.children) > 1:
                raise Exception("Return statement with value in a void function")
            else:
                return None
        right = self.visit(node.children[1])
        if isinstance(right, tc.Array) and isinstance(record["return_type"], type):
            raise Exception("Type mismatch in return statement")
        
        elif not isinstance(right,tc.Array):
            if not isinstance(right, record["return_type"]):
                raise Exception("Type mismatch in return statement")
        return None

    def visit_ConsOp(self, node):
        lexeme = node.children[1].val
        record = self.symtab.lookup(lexeme)
        if record is None:
            raise Exception("Variable ", lexeme, " not declared before cons operation")

        if record["type"] != "array_variable":
            raise Exception(lexeme, " is not declared as a array")

        child = self.visit(node.children[2])
        # TODO make sure its compliant with the changes
        if not isinstance(child, record["object"].datatype):
            raise Exception("Type mismatch in cons operation of ", record["lexeme"])

        return None

    def visit_ThrowStatement(self, node):
        # TODO
        pass

    def visit_TypeDeclaration(self, node):
        # TODO
        pass

    def visit_ExceptionHandling(self, node):
        # TODO
        pass

    def visit_ComplexVal(self, node):
        
        child = self.visit(node.children[0])
        if not isinstance(child, tc.String):
            raise Exception("The first operand must evaluate to a string")
        for i in range(2, len(node.children)):
            self.visit(node.children[i])

        return tc.String()

    def visit_CompCondition(self, node):

        left = self.visit(node.children[0])
        right = self.visit(node.children[2])
        # TODO are we comaprint arrays and tuples - No
        if type(left) != type(right) or (
            not isinstance(left, tc.Datatype) or not isinstance(right, tc.Datatype)
        ):
            raise Exception("Type mismatch in comparison condition")

        return tc.Bool()

    def visit_BoolNode(self, node):
        return tc.Bool()
    
    def visit_HeadNode(self, node):
        
        self.visit(node.children[1])        
        return tc.Number()
        
    def visit_TailNode(self, node):
        
        self.visit(node.children[1]) 
        return tc.Number()
    
    def visit_SliceNode(self, node):
        
        child0 = self.visit(node.children[1])
        child1 = self.visit(node.children[2])
        child2 = self.visit(node.children[3])

        if not isinstance(child1, tc.Number) or not isinstance(child2, tc.Number):
            raise Exception("Inner indices must be numbers")
        
        return child0
        
    def visit_SubstrNode(self, node):
        
        child0 = self.visit(node.children[1])

        if not isinstance(child0, tc.String):
            raise Exception("Referenced object must be a string")
        
        child1 = self.visit(node.children[2])
        child2 = self.visit(node.children[3])

        if not isinstance(child1, tc.Number) or not isinstance(child2, tc.Number):
            raise Exception("Inner indices must be numbers")
        
        return child0

    def visit_UnaryOperation(self, node):
        #! need to check based on post and pre

        if node.children[0] == "~" or node.children[0] == "!":  # pre
            data_type = self.visit(node.children[1])
            if not isinstance(data_type, tc.Number):
                raise Exception("Operation not supported for {}".format(data_type))

        else:  # post
            data_type = self.visit(node.children[0])
            if not isinstance(data_type, tc.Number):
                raise Exception("Operation not supported for {}".format(data_type))

        return tc.Number()
    
    def visit_lenNode(self, node):
        child = self.visit(node.children[1])
        cond = isinstance(child, tc.String) or isinstance(child, tc.Array) or isinstance(child, tc.Tuple)
        if not cond:
            raise Exception("Referenced length function must be a string, array or tuple")
        return tc.Number()

    def get_datatype(self, node):
        # These are tokens

        if node.value == "Integer":
            return tc.Number
        elif node.value == "Bool":
            return tc.Bool
        elif node.value == "String":
            return tc.String
        elif node.value == "Char":
            return tc.Char
        # elif node.__class__.__name__ == 'Function_object':
        #   return tc.Function_object
        # elif node.__class__.__name__ == 'Array':
        #   return tc.Array
        # elif node.__class__.__name__ == 'Tuple':
        #   return tc.Tuple
        # elif node.__class__.__name__ == 'ExceptionType':
        #   return tc.ExceptionType
        else:
            return None
