filetype plugin indent on
syntax on
set title
set tabstop=4
set softtabstop=4
set shiftwidth=4
set noexpandtab
set number relativenumber
set ruler
set scrolloff=8
augroup numbertoggle
autocmd!
autocmd BufEnter,FocusGained,InsertLeave * set relativenumber
autocmd BufLeave,FocusLost,InsertEnter   * set norelativenumber
augroup END
