" zura.vim - Enhanced Syntax highlighting for Zura with custom colors

" Define Zura keywords
syn keyword zuraKeyword const fn have auto loop if else return enum struct typename template
syn keyword zuraType int float bool str char
syn keyword zuraBuiltIn @dis @cast @input @import @extern @call
syn keyword zuraConditional if else
syn keyword zuraLoop loop
syn keyword zuraStatement return
syn keyword zuraModifier const

" Highlight numbers (integers and floats)
syn match zuraNumber /\<\d\+\(\.\d\+\)\?\([eE][+-]\d\+\)\?/

" Highlight strings (single and double quotes)
syn region zuraString start=+"+ skip=+\\"+ end=+"+ contains=zuraEscape
syn region zuraString start=+'+ skip=+\\'+ end=+'+ contains=zuraEscape

" Highlight comments (single-line and multi-line)
syn match zuraComment "#.*$"

" Highlight structs, enums, and function declarations
syn match zuraStruct /\<\(struct\|enum\)\>/
syn match zuraFunction /\<fn\>\s\+\w\+\ze\s*[(]/

" Highlight operators
syn match zuraOperator /[:=(){}\[\],;.+\-*/<>]/

" Highlight variables (avoid matching keywords)
syn match zuraVariable /\<[a-zA-Z_]\w*\>/ contains=zuraKeyword,zuraType

" Custom colors for Zura syntax (Horizon-style palette)
hi def zuraKeyword guifg=#E95678 gui=bold                " Keywords: Warm pink
hi def zuraType guifg=#25B0BC gui=italic                 " Types: Vibrant cyan
hi def zuraBuiltIn guifg=#FAB795 gui=bold,italic         " Built-ins: Peachy orange
hi def zuraConditional guifg=#FAB28E gui=bold           " Conditionals: Muted orange
hi def zuraLoop guifg=#FAB28E gui=bold                  " Loops: Muted orange
hi def zuraStatement guifg=#FFD580 gui=italic           " Statements: Light peach
hi def zuraModifier guifg=#25B0BC gui=bold              " Modifiers: Vibrant cyan
hi def zuraNumber guifg=#E95678                         " Numbers: Warm pink
hi def zuraString guifg=#09F7A0                         " Strings: Soft green
hi def zuraComment guifg=#6C6F93 gui=italic             " Comments: Muted grayish-blue
hi def zuraOperator guifg=#E95678                       " Operators: Warm pink
hi def zuraStruct guifg=#25B0BC gui=bold                " Structs: Vibrant cyan
hi def zuraFunction guifg=#FFD580 gui=bold              " Functions: Light peach
hi def zuraVariable guifg=#FAB                          " Variables: light pink
