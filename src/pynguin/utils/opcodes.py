#  This file is part of Pynguin.
#
#  SPDX-FileCopyrightText: 2019–2024 Pynguin Contributors
#
#  SPDX-License-Identifier: MIT
#

# Idea and structure are taken from the pyChecco project, see:
# https://github.com/ipsw1/pychecco

"""Provides enums for opcode numbers of instructions in bytecode."""

POP_TOP = 1
ROT_TWO = 2
ROT_THREE = 3
DUP_TOP = 4
DUP_TOP_TWO = 5
ROT_FOUR = 6

NOP = 9
UNARY_POSITIVE = 10
UNARY_NEGATIVE = 11
UNARY_NOT = 12

UNARY_INVERT = 15

BINARY_MATRIX_MULTIPLY = 16
INPLACE_MATRIX_MULTIPLY = 17

BINARY_POWER = 19
BINARY_MULTIPLY = 20

BINARY_MODULO = 22
BINARY_ADD = 23
BINARY_SUBTRACT = 24
BINARY_SUBSCR = 25
BINARY_FLOOR_DIVIDE = 26
BINARY_TRUE_DIVIDE = 27
INPLACE_FLOOR_DIVIDE = 28
INPLACE_TRUE_DIVIDE = 29

GET_LEN = 30
MATCH_MAPPING = 31
MATCH_SEQUENCE = 32
MATCH_KEYS = 33
COPY_DICT_WITHOUT_KEYS = 34

WITH_EXCEPT_START = 49
GET_AITER = 50
GET_ANEXT = 51
BEFORE_ASYNC_WITH = 52

END_ASYNC_FOR = 54
INPLACE_ADD = 55
INPLACE_SUBTRACT = 56
INPLACE_MULTIPLY = 57

INPLACE_MODULO = 59
STORE_SUBSCR = 60
DELETE_SUBSCR = 61
BINARY_LSHIFT = 62
BINARY_RSHIFT = 63
BINARY_AND = 64
BINARY_XOR = 65
BINARY_OR = 66
INPLACE_POWER = 67
GET_ITER = 68
GET_YIELD_FROM_ITER = 69

PRINT_EXPR = 70
LOAD_BUILD_CLASS = 71
YIELD_FROM = 72
GET_AWAITABLE = 73

LOAD_ASSERTION_ERROR = 74

INPLACE_LSHIFT = 75
INPLACE_RSHIFT = 76
INPLACE_AND = 77
INPLACE_XOR = 78
INPLACE_OR = 79

RETURN_VALUE = 83
IMPORT_STAR = 84
SETUP_ANNOTATIONS = 85
YIELD_VALUE = 86
POP_BLOCK = 87

POP_EXCEPT = 89

# opcodes below 90 ignore their argument

STORE_NAME = 90
DELETE_NAME = 91
UNPACK_SEQUENCE = 92
FOR_ITER = 93
UNPACK_EX = 94
STORE_ATTR = 95
DELETE_ATTR = 96
STORE_GLOBAL = 97
DELETE_GLOBAL = 98
ROT_N = 99
LOAD_CONST = 100

LOAD_NAME = 101
BUILD_TUPLE = 102
BUILD_LIST = 103
BUILD_SET = 104
BUILD_MAP = 105
LOAD_ATTR = 106
COMPARE_OP = 107
IMPORT_NAME = 108
IMPORT_FROM = 109

JUMP_FORWARD = 110
JUMP_IF_FALSE_OR_POP = 111
JUMP_IF_TRUE_OR_POP = 112
JUMP_ABSOLUTE = 113
POP_JUMP_IF_FALSE = 114
POP_JUMP_IF_TRUE = 115

LOAD_GLOBAL = 116

IS_OP = 117
CONTAINS_OP = 118

RERAISE = 119

JUMP_IF_NOT_EXC_MATCH = 121

SETUP_FINALLY = 122

LOAD_FAST = 124
STORE_FAST = 125
DELETE_FAST = 126

GEN_START = 129

RAISE_VARARGS = 130
CALL_FUNCTION = 131
MAKE_FUNCTION = 132
BUILD_SLICE = 133
LOAD_CLOSURE = 135
LOAD_DEREF = 136
STORE_DEREF = 137
DELETE_DEREF = 138

CALL_FUNCTION_KW = 141
CALL_FUNCTION_EX = 142

SETUP_WITH = 143

LIST_APPEND = 145
SET_ADD = 146
MAP_ADD = 147

LOAD_CLASSDEREF = 148

EXTENDED_ARG = 144

MATCH_CLASS = 152

SETUP_ASYNC_WITH = 154

FORMAT_VALUE = 155
BUILD_CONST_KEY_MAP = 156
BUILD_STRING = 157

LOAD_METHOD = 160
CALL_METHOD = 161
LIST_EXTEND = 162
SET_UPDATE = 163
DICT_MERGE = 164
DICT_UPDATE = 165


OP_UNARY = (
    UNARY_POSITIVE,
    UNARY_NEGATIVE,
    UNARY_NOT,
    UNARY_INVERT,
    GET_ITER,
    GET_YIELD_FROM_ITER,
)
OP_BINARY = (
    BINARY_POWER,
    BINARY_MULTIPLY,
    BINARY_MATRIX_MULTIPLY,
    BINARY_FLOOR_DIVIDE,
    BINARY_TRUE_DIVIDE,
    BINARY_MODULO,
    BINARY_ADD,
    BINARY_SUBTRACT,
    BINARY_LSHIFT,
    BINARY_RSHIFT,
    BINARY_AND,
    BINARY_XOR,
    BINARY_OR,
)
OP_INPLACE = (
    INPLACE_POWER,
    INPLACE_MULTIPLY,
    INPLACE_MATRIX_MULTIPLY,
    INPLACE_FLOOR_DIVIDE,
    INPLACE_TRUE_DIVIDE,
    INPLACE_MODULO,
    INPLACE_ADD,
    INPLACE_SUBTRACT,
    INPLACE_LSHIFT,
    INPLACE_RSHIFT,
    INPLACE_AND,
    INPLACE_XOR,
    INPLACE_OR,
)
OP_COMPARE = (COMPARE_OP, IS_OP, CONTAINS_OP)
OP_LOCAL_ACCESS = (STORE_FAST, LOAD_FAST, DELETE_FAST)
OP_NAME_ACCESS = (STORE_NAME, LOAD_NAME, DELETE_NAME)
OP_GLOBAL_ACCESS = (STORE_GLOBAL, LOAD_GLOBAL, DELETE_GLOBAL)
OP_DEREF_ACCESS = (STORE_DEREF, LOAD_DEREF, DELETE_DEREF, LOAD_CLASSDEREF)
OP_ATTR_ACCESS = (STORE_ATTR, LOAD_ATTR, DELETE_ATTR, IMPORT_FROM, LOAD_METHOD)
OP_SUBSCR_ACCESS = (STORE_SUBSCR, DELETE_SUBSCR, BINARY_SUBSCR)
OP_IMPORT_NAME = (IMPORT_NAME,)
OP_ABSOLUTE_JUMP = (
    JUMP_IF_FALSE_OR_POP,
    JUMP_IF_TRUE_OR_POP,
    JUMP_ABSOLUTE,
    POP_JUMP_IF_FALSE,
    POP_JUMP_IF_TRUE,
    JUMP_IF_NOT_EXC_MATCH,
)
OP_RELATIVE_JUMP = (
    FOR_ITER,
    JUMP_FORWARD,
    SETUP_FINALLY,
    SETUP_WITH,
    SETUP_ASYNC_WITH,
)
OP_CALL = (CALL_FUNCTION, CALL_FUNCTION_KW, CALL_FUNCTION_EX, CALL_METHOD, YIELD_FROM)
OP_RETURN = (RETURN_VALUE, YIELD_VALUE)

TRACED_INSTRUCTIONS = (
    OP_UNARY
    + OP_BINARY
    + OP_INPLACE
    + OP_COMPARE
    + OP_LOCAL_ACCESS
    + OP_NAME_ACCESS
    + OP_GLOBAL_ACCESS
    + OP_DEREF_ACCESS
    + OP_ATTR_ACCESS
    + OP_SUBSCR_ACCESS
    + OP_IMPORT_NAME
    + OP_ABSOLUTE_JUMP
    + OP_RELATIVE_JUMP
    + OP_CALL
    + OP_RETURN
)

MEMORY_USE_INSTRUCTIONS = (
    LOAD_FAST,
    LOAD_NAME,
    LOAD_GLOBAL,
    LOAD_ATTR,
    LOAD_DEREF,
    BINARY_SUBSCR,
    LOAD_METHOD,
    IMPORT_FROM,
    LOAD_CLOSURE,
    LOAD_CLASSDEREF,
)
MEMORY_DEF_INSTRUCTIONS = (
    STORE_FAST,
    STORE_NAME,
    STORE_GLOBAL,
    STORE_DEREF,
    STORE_ATTR,
    STORE_SUBSCR,
    BINARY_SUBSCR,
    DELETE_FAST,
    DELETE_NAME,
    DELETE_GLOBAL,
    DELETE_ATTR,
    DELETE_SUBSCR,
    DELETE_DEREF,
    IMPORT_NAME,
)  # compensate incorrect stack effect for IMPORT_NAME
COND_BRANCH_INSTRUCTIONS = (
    POP_JUMP_IF_TRUE,
    POP_JUMP_IF_FALSE,
    JUMP_IF_TRUE_OR_POP,
    JUMP_IF_FALSE_OR_POP,
    JUMP_IF_NOT_EXC_MATCH,
    FOR_ITER,
)
