import os
import subprocess
import time

def get_git_last_commit_time(repo_dir):
    """
    获取指定Git仓库的最新提交时间
    """
    try:
        # 获取最新提交的时间戳
        result = subprocess.run(
            ['git', 'log', '-1', '--format=%ct'], 
            cwd=repo_dir, 
            text=True, 
            capture_output=True,
            check=True
        )
        return int(result.stdout.strip())
    except subprocess.CalledProcessError:
        return None  # 如果不是Git仓库，返回None

def get_folder_last_modified_time(repo_dir):
    """
    获取文件夹的最后修改时间（UNIX时间戳）
    """
    return os.path.getmtime(repo_dir)

def update_folder_timestamp(repo_dir, timestamp):
    """
    使用给定的时间戳更新文件夹的修改时间
    """
    subprocess.run(['touch', '-t', time.strftime('%Y%m%d%H%M.%S', time.localtime(timestamp)), repo_dir])

def process_repositories(base_dir):
    """
    遍历给定目录下的所有子目录，查找Git仓库并更新文件夹的修改时间
    """
    for root, dirs, files in os.walk(base_dir):
        # 检查每个子目录是否是Git仓库
        if '.git' in dirs:  # 判断是否是Git仓库
            commit_time = get_git_last_commit_time(root)
            if commit_time:
                # 获取当前文件夹的修改时间
                current_folder_time = get_folder_last_modified_time(root)
                
                # 如果文件夹的修改时间与最后提交时间相同，则跳过
                if current_folder_time == commit_time:
                    continue  # 如果时间相同，就跳过这个仓库的更新
                
                # 打印仓库的最后提交时间
                print(f"Last commit time for {root}: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(commit_time))}")
                
                # 更新文件夹的时间戳
                update_folder_timestamp(root, commit_time)
                print(f"Updated folder timestamp for {root} to the last commit time.")
            else:
                print(f"{root} is not a valid Git repository.")

if __name__ == "__main__":
    base_dir = "/Users/abel/AbelProject"  # 你的Git仓库根目录
    process_repositories(base_dir)
