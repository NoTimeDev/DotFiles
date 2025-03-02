" Syntax file for Zed
if exists("b:current_syntax")
  finish
endif

syntax match ZedDef /[#][0-9A-za-z_.+:><-]*/
highlight ZedDef guifg=#F5A6F5

syntax keyword zedKeyword import as def return func mut const from extern static

highlight zedKeyword ctermfg=5 guifg=#cba6f7 " Catppuccin Mauve (Purple)

" `mut` and `const` (red)
" syntax keyword zedStorage mut const 
" highlight zedStorage ctermfg=1 guifg=#f38ba8 " Catppuccin Red

" Comments (// for single-line, /* */ for multi-line, grey/light color)
syntax match zedComment "//.*$"
syntax match zedBracket "\v[\[\]{}()]"
syntax region zedCommentBlock start="/\*" end="\*/"

highlight zedComment ctermfg=8 guifg=#a6adc8 " Catppuccin Subtext0 (Grey/Light Color)
highlight zedBracket ctermfg=8 guifg=#a6adc8 " Catppuccin Subtext0 (Grey/Light Color)
highlight zedCommentBlock ctermfg=8 guifg=#a6adc8 " Catppuccin Subtext0 (Grey/Light Color)

" Numbers (supports hex, underscores, and floats)
syntax match zedNumber "\v0x[0-9A-Fa-f_]+"
syntax match zedNumber "\v\d+(_\d+)*(\.\d+(_\d+)*)?"
highlight zedNumber ctermfg=9 guifg=#f8bd96 " Catppuccin Orange

" Highlight strings (single and double quotes)
syntax region zedString start=+"+ skip=+\\"+ end=+"+ contains=zuraEscape
syntax region zedString start=+'+ skip=+\\'+ end=+'+ contains=zuraEscape

highlight zedString ctermfg=Green guifg=#98C379

" Variables (highlighted in blue)
syntax match zedVariable /\v<[a-zA-Z_][a-zA-Z0-9_]*>/
" highlight zedVariable ctermfg=4 guifg=#9fc5e8 " Catppuccin Blue

" Operators (+, -, *, /, etc.) (orange)
" syntax match zedOperator "\v[+\-*/%=<>!&|^~?]"
" highlight zedOperator ctermfg=3 guifg=#f9e2af " Catppuccin Yellow

let b:current_syntax = "zsjsjjs"

