# llm

## 准备工作
### 新的征程已经开始,溜溜梅宇宙队冲鸭
<details>
  
<summary>课程安排</summary>

【教程地址】https://datawhalechina.github.io/llm-universe/  
【开源项目仓库】https://github.com/datawhalechina/llm-universe  
【小程序使用说明】https://mp.weixin.qq.com/s/iPmzb72Yk0mhIA2NYezXDg  
【学习者手册】 https://mp.weixin.qq.com/s/pwWg0w1DL2C1i_Hs3SZedg  

Task01:第一章LLM介绍  
截止时间06月20日03:00

Task02:第二章 使用 LLM API 开发应用  
截止时间06月23日03:00

Task03:第三章 搭建知识库  
截止时间06月25日03:00

Task04:第四章 构建 RAG 应用  
截止时间06月27日03:00

Task05:第五章 系统评估与优化  
截止时间06月29日03:00

Task06:开源 RAG 项目学习  
截止时间07月01日03:00
</details>





<details>
  
<summary>部署wsl2子系统</summary>

### 部署wsl2子系统
启用wsl子系统
```powershell
wsl --install --no-distribution
```
Microsoft Store下载自己需要的Linux发行版(本文基于Ubuntu-24.04 LTS)
```bash
# .wslconfig文件放在当前用户文件夹内
[wsl2]
[experimental]
# 自动释放内存
autoMemoryReclaim=gradual
# 自动释放磁盘
# sparseVhd=true
# 网络自动映射
networkingMode=mirrored
dnsTunneling=true
firewall=true
```

</details>

<details>
  
<summary>修改ubuntu24.04 apt 源</summary>

### 修改ubuntu24.04 apt 源
```bash
sudo vim /etc/apt/sources.list.d/ubuntu.sources
```
```bash
Types: deb
URIs: https://mirrors.cernet.edu.cn/ubuntu
Suites: noble noble-updates noble-backports
Components: main restricted universe multiverse
Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg

Types: deb
URIs: http://security.ubuntu.com/ubuntu/
Suites: noble-security
Components: main restricted universe multiverse
Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg
```
```bash
sudo apt update && sudo apt upgrade
```
</details>


<details>
  
<summary>安装zsh + ohmyzsh + power10k + 字体</summary>

### 安装zsh + ohmyzsh + power10k + 字体

安装`zsh`
```bash
sudo apt install zsh
```
设置zsh为默认shell,执行后重启终端,选择2创建默认推荐的`.zshrc`
```bash
chsh -s $(which zsh)
```
安装`ohmyzsh`
```bash
sh -c "$(wget -O- https://install.ohmyz.sh)"
```
防止产生`.zcomdump*`在根目录
```bash
sed -i -e "/source \$ZSH\/oh-my-zsh.sh/i export ZSH_COMPDUMP=\$ZSH\/cache\/.zcompdump-\$HOST" ~/.zshrc
```
安装`power10k`,推荐的字体可以参考[推荐字体](https://github.com/romkatv/powerlevel10k?tab=readme-ov-file#meslo-nerd-font-patched-for-powerlevel10k)

```bash
git clone --depth=1 https://gitee.com/romkatv/powerlevel10k.git ~/powerlevel10k
echo 'source ~/powerlevel10k/powerlevel10k.zsh-theme' >>~/.zshrc
```
需要修改终端-默认值-外观-字体为推荐字体才能正常显示符号
</details>

<details>
  
<summary>安装miniconda3 + python</summary>

### 安装miniconda3 + python
```bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
```
将conda写入`zsh`和`bash`
```bash
~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh
```
修改`conda sources`
```bash
vim ~/.condarc
```
```bash
channels:
  - defaults
show_channel_urls: true
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
```
清除conda索引缓存
```bash
conda clean -i
```

### Make conda useful again（MCUA）

`powershell` 版本输入`notepad $$profile`编辑

```powershell
function rmenv($envName) {
    conda remove -n $envName --all -y
    conda env list
}

function mkenv($envName,[string]$pythonVer = "3.11"){
    conda create -n $envName python=$pythonVer -y
    conda activate $envName
}
```
`bash`版本`vim ~/.bashrc`或者`vim ~/.zshrc`

```bash
# 定义 rmenv 函数，用于移除 Conda 环境
rmenv() {
    # 使用 conda remove 命令移除指定的环境及其所有包
    conda remove -n "$1" --all -y
    # 列出所有 Conda 环境
    conda env list
}

# 定义 mkenv 函数，用于创建新的 Conda 环境
mkenv() {
    # 使用 conda create 命令创建新的环境，并指定 Python 版本
    # 默认 Python 版本为 3.11，如果提供了参数，则使用提供的版本
    envName="$1"
    pythonVer="${2:-3.11}"
    conda create -n "$envName" python="$pythonVer" -y
    # 激活新创建的环境
    conda activate "$envName"
}
```
修改`pip源`
```bash
pip config set global.index-url https://mirrors.bfsu.edu.cn/pypi/web/simple
```

</details>



## llm项目学习
<details>

<summary>Day 1</summary>

- 介绍了LLM是什么,国内网常见的大模型有哪些
- 引出LLM的缺点引入了检索增强生成(RAG)
- 如何快速搭建属于自己的LLM--LanChain
- 环境配置  

clone项目到本地,国内直接clone大概率是没速度的,直接从镜像克隆算了
```bash
git clone https://mirror.ghproxy.com/https://github.com/datawhalechina/llm-universe.git
```
新建conda环境
```bash
conda create -n llm python=3.11 -y
conda activate llm
pip install -r requirement.txt

```
手动下载`nltk`数据,`nltk_data`在用户路径根目录,文件结构如下,可以通过指令`python -m nltk.downloader popular `下载流行的nltk数据
```bash
nltk_data
└── corpora
    ├── cmudict
    │   ├── README
    │   └── cmudict
    ├── cmudict.zip
    ├── gazetteers
    │   ├── LICENSE.txt
    │   ├── caprovinces.txt
    │   ├── countries.txt
    │   ├── isocountries.txt
    │   ├── mexstates.txt
    │   ├── nationalities.txt
    │   ├── uscities.txt
    │   ├── usstateabbrev.txt
    │   └── usstates.txt
    ├── gazetteers.zip
    ├── genesis
    │   ├── README
    │   ├── english-kjv.txt
    │   ├── english-web.txt
    │   ├── finnish.txt
    │   ├── french.txt
    │   ├── german.txt
    │   ├── lolcat.txt
    │   ├── portuguese.txt
    │   └── swedish.txt
    └── genesis.zip
```
手动下载`nltk_data`, 可能需要先安装`unzip`
```bash
git clone https://gitee.com/yzy0612/nltk_data.git  --branch gh-pages
cd nltk_data
mv packages/*  ./
cd tokenizers
unzip punkt.zip
cd ../taggers
unzip averaged_perceptron_tagger.zip
```
</details>