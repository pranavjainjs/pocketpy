from typing import overload

def malloc(size: int) -> 'void_p': ...
def free(ptr: 'void_p') -> None: ...
def sizeof(type: str) -> int: ...
def memset(ptr: 'void_p', value: int, size: int) -> None: ...
def memcpy(dst: 'void_p', src: 'void_p', size: int) -> None: ...

class void_p:
    def __init__(self, addr: int): ...
    def __add__(self, i: int) -> 'void_p': ...
    def __sub__(self, i: int) -> 'void_p': ...
    def __eq__(self, other: 'void_p') -> bool: ...
    def __ne__(self, other: 'void_p') -> bool: ...

    def hex(self) -> str: ...

    def read_char(self) -> int: ...
    def read_uchar(self) -> int: ...
    def read_short(self) -> int: ...
    def read_ushort(self) -> int: ...
    def read_int(self) -> int: ...
    def read_uint(self) -> int: ...
    def read_long(self) -> int: ...
    def read_ulong(self) -> int: ...
    def read_longlong(self) -> int: ...
    def read_ulonglong(self) -> int: ...
    def read_float(self) -> float: ...
    def read_double(self) -> float: ...
    def read_bool(self) -> bool: ...
    def read_void_p(self) -> 'void_p': ...
    def read_bytes(self, size: int) -> bytes: ...
    def read_struct(self, size: int) -> 'struct': ...

    def write_char(self, value: int) -> None: ...
    def write_uchar(self, value: int) -> None: ...
    def write_short(self, value: int) -> None: ...
    def write_ushort(self, value: int) -> None: ...
    def write_int(self, value: int) -> None: ...
    def write_uint(self, value: int) -> None: ...
    def write_long(self, value: int) -> None: ...
    def write_ulong(self, value: int) -> None: ...
    def write_longlong(self, value: int) -> None: ...
    def write_ulonglong(self, value: int) -> None: ...
    def write_float(self, value: float) -> None: ...
    def write_double(self, value: float) -> None: ...
    def write_bool(self, value: bool) -> None: ...
    def write_void_p(self, value: 'void_p') -> None: ...
    def write_bytes(self, value: bytes) -> None: ...
    def write_struct(self, value: 'struct') -> None: ...

class struct:
    @overload
    def __init__(self, size: int): ...
    @overload
    def __init__(self, buffer: bytes): ...

    def addr(self) -> 'void_p': ...
    def copy(self) -> 'struct': ...
    def size(self) -> int: ...
    def __eq__(self, other: 'struct') -> bool: ...
    def __ne__(self, other: 'struct') -> bool: ...

    def read_char(self, offset=0) -> int: ...
    def read_uchar(self, offset=0) -> int: ...
    def read_short(self, offset=0) -> int: ...
    def read_ushort(self, offset=0) -> int: ...
    def read_int(self, offset=0) -> int: ...
    def read_uint(self, offset=0) -> int: ...
    def read_long(self, offset=0) -> int: ...
    def read_ulong(self, offset=0) -> int: ...
    def read_longlong(self, offset=0) -> int: ...
    def read_ulonglong(self, offset=0) -> int: ...
    def read_float(self, offset=0) -> float: ...
    def read_double(self, offset=0) -> float: ...
    def read_bool(self, offset=0) -> bool: ...
    def read_void_p(self, offset=0) -> 'void_p': ...

    def write_char(self, value: int, offset=0) -> None: ...
    def write_uchar(self, value: int, offset=0) -> None: ...
    def write_short(self, value: int, offset=0) -> None: ...
    def write_ushort(self, value: int, offset=0) -> None: ...
    def write_int(self, value: int, offset=0) -> None: ...
    def write_uint(self, value: int, offset=0) -> None: ...
    def write_long(self, value: int, offset=0) -> None: ...
    def write_ulong(self, value: int, offset=0) -> None: ...
    def write_longlong(self, value: int, offset=0) -> None: ...
    def write_ulonglong(self, value: int, offset=0) -> None: ...
    def write_float(self, value: float, offset=0) -> None: ...
    def write_double(self, value: float, offset=0) -> None: ...
    def write_bool(self, value: bool, offset=0) -> None: ...
    def write_void_p(self, value: 'void_p', offset=0) -> None: ...

def char_(val: int) -> struct: ...
def uchar_(val: int) -> struct: ...
def short_(val: int) -> struct: ...
def ushort_(val: int) -> struct: ...
def int_(val: int) -> struct: ...
def uint_(val: int) -> struct: ...
def long_(val: int) -> struct: ...
def ulong_(val: int) -> struct: ...
def longlong_(val: int) -> struct: ...
def ulonglong_(val: int) -> struct: ...
def float_(val: float) -> struct: ...
def double_(val: float) -> struct: ...
def bool_(val: bool) -> struct: ...

char_p = void_p
uchar_p = void_p
short_p = void_p
ushort_p = void_p
int_p = void_p
uint_p = void_p
long_p = void_p
ulong_p = void_p
longlong_p = void_p
ulonglong_p = void_p
float_p = void_p
double_p = void_p
bool_p = void_p

class array(struct):
    count: int
    item_size: int

    def __new__(cls, count: int, item_size: int): ...
    def __getitem__(self, index: int) -> struct: ...
    def __setitem__(self, index: int, value: struct) -> None: ...
    def __len__(self) -> int: ...

from typing import Generic, TypeVar

T = TypeVar('T')

class _StructLike(Generic[T]):
    def to_struct(self) -> struct: ...
    @classmethod
    def from_struct(cls, s: struct) -> T: ...

    def addr(self) -> '_Pointer[T]': ...
    def sizeof(self) -> int: ...
    def copy(self) -> T: ...
    def __eq__(self, other: T) -> bool: ...
    def __ne__(self, other: T) -> bool: ...

class _Pointer(Generic[T], void_p):
    pass
