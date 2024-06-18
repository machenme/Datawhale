## 部署wsl2子系统
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
