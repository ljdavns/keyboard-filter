import PyInstaller.__main__

PyInstaller.__main__.run([
    'keyboard_filter.py',
    '--onefile',
    '--uac-admin',        # 请求管理员权限
    '--name=KeyFilter',
    '--hidden-import=keyboard',
])