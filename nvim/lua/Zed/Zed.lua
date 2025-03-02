local RetTable = {}

function RetTable.HighLight(FilePath)

    local char = vim.v.char
    local row, col = unpack(vim.api.nvim_win_get_cursor(0))
    local lines = vim.api.nvim_buf_get_lines(0, 0, -1, false)
    
    local line = lines[row] or ""

    local newline = line:sub(1, col) .. char .. line:sub(col + 1)
    lines[row] = newline
    
   -- local lines = vim.api.nvim_buf_get_lines(0, 0, -1, false)
    

    local filele = io.open("/home/devvy/.config/nvim/lua/Zed/Lex.txt", "w")
    if not filele then
        print('Err')
    end

    for _, line in ipairs(lines) do 
        filele:write(line .. "\n")

    end
    filele:close()


	print(vim.fn.system("cd"))

	local Info = vim.fn.system("python ZedLexer.py " .. FilePath)

    vim.cmd("highlight ZedString guifg=#A6E3A1")
	vim.cmd("highlight ZedNumber guifg=#FAB387")
    vim.cmd("highlight ZedLet guifg=#F38BA8")
	vim.cmd("highlight link ZedComment Comment")
	vim.cmd("highlight link ZedKeyword Keyword")
    vim.cmd("highlight ZedType guifg=#89DCEB")
    vim.cmd("highlight ZedVar guifg=#74C7EC")
    vim.cmd("highlight YellowBrack guifg=#FEE842")
    vim.cmd("highlight PurpleBrack guifg=#FE42CF")
    vim.cmd("highlight SlashCode guifg=#F5C2E7")
    
	local bufnr = vim.api.nvim_get_current_buf()
	local ns_id = vim.api.nvim_create_namespace("MyHighlightNamespace")
        
    vim.api.nvim_buf_clear_namespace(0, ns_id, 0, -1)
	local file = io.open("/home/devvy/.config/nvim/lua/Zed/ZedLight.txt", "r")
	if not file then
		print("could not find file")
	end
	local chunk = {}
	for line in file:lines() do
		table.insert(chunk, line)
		if #chunk == 4 then
			vim.api.nvim_buf_add_highlight(bufnr, ns_id, chunk[4], tonumber(chunk[1]), tonumber(chunk[2]), tonumber(chunk[3])) -- Line 1 is index 0 in Lua
			chunk = {}
		end
	end 


	print(Info)
	file:close()
end

function RetTable.CheckIfFile(filename)
	local File = io.open(filename)
	if File then
		File:close()
		return true
	else
		return false
	end
end

return RetTable
