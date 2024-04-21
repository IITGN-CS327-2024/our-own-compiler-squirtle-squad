 (module
                    ;; Memory with 1 page (64KB)
                    (memory (export "memory") 1)

                    (func $store_value_at_address (param $value i32) (param $address i32)
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
                    )
              
                    (func $logical_not (param $a i32) (result i32)
                        ;; Convert $a to 0 or 1 (0 if $a is zero, 1 otherwise)
                        local.get $a
                        i32.const 0
                        i32.eq
                    )
              
                    (func $logical_and (param $a i32) (param $b i32) (result i32)
                        ;; Perform bitwise AND
                        local.get $a
                        local.get $b
                        i32.and
                        ;; Convert result to 0 or 1 (0 if result is zero, 1 otherwise)
                        i32.const 1
                        i32.eq
                    )
        
(func $add(param $a i32)(param $b i32)(result i32)
(local $var i32)
local.get $a


local.get $b


i32.add




)
(export "add" (func $add))


(func $sub(param $a i32)(param $b i32)(result i32)
(local $var i32)
local.get $a


local.get $b


i32.sub




)
(export "sub" (func $sub))


(func $mul(param $a i32)(param $b i32)(result i32)
(local $var i32)
local.get $a


local.get $b


i32.mul




)
(export "mul" (func $mul))


(func $mod(param $a i32)(param $b i32)(result i32)
(local $var i32)
local.get $a


local.get $b


i32.rem_s




)
(export "mod" (func $mod))


(func $div(param $a i32)(param $b i32)(result i32)
(local $var i32)
local.get $a


local.get $b


i32.div_s




)
(export "div" (func $div))


)
