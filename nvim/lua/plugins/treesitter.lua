return {
    {
        "nvim-treesitter/nvim-treesitter",
        build = ":TSUpdate",

        config = function()
            local config = require("nvim-treesitter.configs")
            config.setup({
                ensure_installed = {
                    "lua",
                    "python",
                    "cpp",
                    "asm",
                    "c",
                    "json",
                    "llvm",
                    "rust",
                },
                highlight = { enable = true },
                indent = { enable = true },
            })
        end
    },
    {
        "WhoIsSethDaniel/mason-tool-installer.nvim",
        config = function()
            require("mason-tool-installer").setup({
                'black',
                'debugpy',
                'flake8',
                'isort',
                'ruff',
                'mypy',
                'pylint'
            })
        end
    }
}
