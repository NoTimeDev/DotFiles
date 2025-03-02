vim.opt.tabstop = 4
vim.opt.shiftwidth = 4
vim.opt.expandtab = true
vim.wo.number = true
vim.o.wrap = false
vim.o.updatetime = 1000




local Zed = require("Zed.Zed")

--vim.filetype.add({
  --  extension = {
    --    Z = "zlang"
    --}
--})

vim.cmd(":set hlsearch!")
-- auto-save-made by a dumbass!
vim.api.nvim_create_autocmd({ "CursorHold", "CursorHoldI" }, {
    pattern = "*",
    callback = function()
        local File = vim.fn.expand("%:p")
        --print("CFile: ", File)
        local bufname = vim.api.nvim_buf_get_name(0)
        if bufname ~= "" and vim.fn.filereadable(bufname) == 1 then
            vim.cmd("w!")
        end
    end,
})

--zed
--"TextChangedI", "TextChanged", "CursorHold", "CursorHoldI"-vim.g.python3_host_prog = "C:\\Users\\Dev\\AppData\\Local\\Programs\\Python\\Python313\\python.exe"
vim.api.nvim_create_autocmd({"InsertCharPre", "CursorMovedI"}, {
    pattern = "*.z",
    callback = function(args)
        Zed.HighLight(vim.fn.expand("%:p"))
   end
})

-----------------------------------------------------------
require(".config.lazy")
