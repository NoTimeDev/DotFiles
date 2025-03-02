return {
    "catppuccin/nvim",
    name = "catppuccin",
    priority = 1000,
    config = function()
        require("catppuccin").setup({
            transparent_background = true, -- Enable transparency
            integrations = {
                neotree = true, -- Enable Neo-tree integration
                telescope = true,
                cmp = true,
                lsp_saga = true,
            },
        })
        vim.cmd.colorscheme "catppuccin" -- Set the colorscheme
    end

}

--
--return {
	--"catppuccin/nvim",
	--name = "catppuccin",
	--priority = 1000,
    --opt = { 
      --  transparent_background = true,
    --},
  --  config = function()
--	    vim.cmd.colorscheme("catppuccin")
--	end,
    


--}
