if exists("b:current_syntax")
  finish
endif

syntax keyword zrKeyword start end ftui ftsi uitf sitf ftrunc ftext to call zext sext load ret add sub mul div udiv umul mod umod trunc fadd fmul fdiv extern def geteptr adr global
syntax keyword zrType f32 f64 i32 i16 i64 i8 i1 
syntax match zrComment "#.*$"
syntax match zrNumber "\<\d\+\>"
syntax match zrString /".\{-}"/
syntax match zrString /'.\{-}'/
syntax match zrDollarVar /[$@?][0-9A-za-z_.+:><-]*/

highlight zrDollarVar ctermfg=Blue guifg=#569CD6
highlight link zrKeyword Keyword
highlight zrString ctermfg=Green guifg=#98C379
highlight link zrType Type
highlight link zrNumber Number
highlight link zrComment Comment

let b:current_syntax = "zr"

