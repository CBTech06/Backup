
""" -- [VIMPLUG] --
call plug#begin()
  	Plug 'sheerun/vim-polyglot'
        Plug 'vim-airline/vim-airline'
        Plug 'vim-airline/vim-airline-themes'
        Plug 'ryanoasis/vim-devicons'
        Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
        Plug 'vim-syntastic/syntastic'
        Plug 'junegunn/fzf.vim'
        Plug 'chrisbra/Colorizer'
  	    Plug 'honza/vim-snippets'
        Plug 'sainnhe/sonokai'
  	    Plug 'mattn/vim-gist'
        Plug 'mattn/webapi-vim'
        Plug 'vimwiki/vimwiki'
call plug#end()

"""  -- [OTHER CFG] --
syntax on                               " Enables syntax highlighing
set hidden                              " Required to keep multiple buffers open multiple buffers
set nowrap                              " Display long lines as just one line
set encoding=utf-8                      " The encoding displayed 
set pumheight=10                        " Makes popup menu smaller
set fileencoding=utf-8                  " The encoding written to file
set cmdheight=2                         " More space for displaying messages
set splitbelow                          " Horizontal splits will automatically be below
set splitright                          " Vertical splits will automatically be to the right
set smarttab                            " Makes tabbing smarter will realize you have 2 vs 4
set expandtab                           " Converts tabs to spaces
set smartindent                         " Makes indenting smart
set autoindent                          " Good auto indent
set laststatus=2                        " Always display the status line
set number                              " Line numbers
set nocursorline                        " Enable highlighting of the current line
set showtabline=2                       " Always show tabs 
set nobackup                            " This is recommended by coc
set clipboard=unnamedplus               " Copy paste between vim and everything else
set noswapfile
set incsearch
set ignorecase
set viewoptions =cursor,folds,slash,unix
set sessionoptions=folds
set foldenable
" set mouse=a                           " Enable your mouse
"set ruler              			          " Show the cursor position all the time
"set foldmethod=syntax
" filetype plugin on
"set relativenumber
set nocompatible
set t_Co=256                            " Support 256 colors
set background=dark                     " tell vim what the background color looks like

if has('termguicolors')
        set termguicolors
endif

""" -- [SYNTASTIC] --
""" Install cpplint pip install cpplint
let g:syntastic_cpp_checkers = ['cpplint']
let g:syntastic_c_checkers = ['cpplint']
let g:syntastic_cpp_cpplint_exec = 'cpplint'
" The following two lines are optional. Configure it to your liking!
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0

""" -- [COLORSCHEME] --
let g:sonokai_style = 'mais'
let g:sonokai_enable_italic = 1
let g:sonokai_disable_italic_comment = 1
colorscheme PaperColor
let g:airline_theme='soda'
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#buffer_nr_show = 1

"highlight Pmenu guibg=white guifg=black gui=bold
"highlight Comment gui=bold
"highlight Normal guifg=cyan
"highlight NonText guibg=none

""" -- [CUSTOM MAPPINGS] --
let mapleader=","
" nmap <leader>q :NERDTreeToggle<CR>
nnoremap <leader>w% :vsplit 
nnoremap <leader>w" :split 

nmap <S-Tab> :bprevious<CR>
nnoremap <leader>re :edit $MYVIMRC<CR>
nnoremap <leader>rs :source %<CR>
nnoremap <leader>c :Colors<CR>
cmap w!! w !sudo tee %

"" -- [COLORIZER] --
nmap <leader>k :ColorToggle<CR>       

""" -- [FOLD METHOD] --
inoremap <F9> <C-O>za
nnoremap <F9> za
onoremap <F9> <C-C>za
vnoremap <F9> zf

autocmd BufWinLeave,BufLeave *.*  mkview
autocmd BufWinEnter *.* silent! loadview

""" -- [TERMINAL] --
map <Leader>tt :vnew term://zsh<CR>
tnoremap <C-w>c <C-\><C-n>:q!<CR>

""" -- [ SPLIT MOVE] --
nnoremap <leader>w <C-w>

""" -- [SPLIT RESIZING] -- 
nnoremap <C-Left> :vertical resize +3<CR>
nnoremap <C-Right> :vertical resize -3<CR>
nnoremap <C-Up> :resize +3<CR>
nnoremap <C-Down> :resize -3<CR>
nnoremap <Leader>th <C-w>t<C-w>H
nnoremap <Leader>tk <C-w>t<C-w>K

""" -- [VIM WIKI] --
let g:vimwiki_list = [{'path': '/mnt/Notes/',
                      \ 'syntax': 'markdown', 'ext' : '.md'}]
"let g:vimwiki_folding = 'custom'
let g:vimwiki_hl_headers = 1
"let g:vimwiki_listsyms = '✗○◐●✓'

""" -- [FZF / RIPGREP] -- 
let g:fzf_action = {
  \ 'ctrl-t': 'tab split',
  \ 'ctrl-s': 'split',
  \ 'ctrl-v': 'vsplit' }
let g:fzf_colors =
\ { 'fg':      ['fg', 'Normal'],
  \ 'bg':      ['bg', 'Normal'],
  \ 'hl':      ['fg', 'Comment'],
  \ 'fg+':     ['fg', 'CursorLine', 'CursorColumn', 'Normal'],
  \ 'bg+':     ['bg', 'CursorLine', 'CursorColumn'],
  \ 'hl+':     ['fg', 'Statement'],
  \ 'info':    ['fg', 'Type'],
  \ 'border':  ['fg', 'Ignore'],
  \ 'prompt':  ['fg', 'Character'],
  \ 'pointer': ['fg', 'Exception'],
  \ 'marker':  ['fg', 'Keyword'],
  \ 'spinner': ['fg', 'Label'],
  \ 'header':  ['fg', 'Comment'] }

let g:fzf_history_dir = '~/.local/share/fzf-history'

map <leader>f :Files<CR>
map <leader>b :Buffers<CR>
nnoremap <leader>g :Rg<CR>
nnoremap <leader>t :Tags<CR>
nnoremap <leader>m :Marks<CR>

