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
        
(func $sort(param $yashraj i32)(param $length i32)
(local $i i32)
(local $j i32)
(local $temp i32)
(local $var i32)
i32.const 0


local.set $temp


i32.const 0


local.set $i


(loop $apnaloop
local.get $i


local.get $length


i32.const 1


i32.sub


i32.lt_s


i32.const 1
i32.eq
(if
(then
i32.const 0


local.set $j


(loop $apnaloop
local.get $j


local.get $length


local.get $i


i32.sub


i32.const 1


i32.sub


i32.lt_s


i32.const 1
i32.eq
(if
(then
local.get $j


i32.const 0
(call $arrindexing)
(call $loadValueFromMemory)
local.get $j


i32.const 1


i32.add


i32.const 0
(call $arrindexing)
(call $loadValueFromMemory)
i32.gt_s


i32.const 1
i32.eq
(if
(then
local.get $yashraj
local.get $j


i32.const 4
i32.mul
i32.add
local.set $var
local.get $var
(call $loadValueFromMemory)
local.set $temp
local.get $yashraj
local.get $j


i32.const 1


i32.add


i32.const 4
i32.mul
i32.add
local.set $var
local.get $var
(call $loadValueFromMemory)
local.get $yashraj
local.get $j


i32.const 4
i32.mul
i32.add
local.set $var
local.get $var
(call $store_value_at_address)
local.get $temp


local.get $yashraj
local.get $j


i32.const 1


i32.add


i32.const 4
i32.mul
i32.add
local.set $var
local.get $var
(call $store_value_at_address)
)
)


i32.const 1
local.get $j
i32.add
local.set $j


br $apnaloop
)
)
)


i32.const 1
local.get $i
i32.add
local.set $i


br $apnaloop
)
)
)


)
(export "sort" (func $sort))


)
