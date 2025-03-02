return {
	"nvim-neo-tree/neo-tree.nvim",
	branch = "v3.x",
	dependencies = {
		"nvim-lua/plenary.nvim",
		"nvim-tree/nvim-web-devicons",
		"MunifTanjim/nui.nvim",
	},
	config = function()
		vim.keymap.set("n", "<leader>nt", ":Neotree <CR>", {})
        require('neo-tree').setup({
            filesystem={
                follow_current_file = true,
                use_libuv_file_watcher = true,
                hijack_netrw_behaviour = "open_current"
            }
        })
    end,
}
