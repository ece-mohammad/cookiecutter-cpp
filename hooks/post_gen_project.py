"""Post-project generation hooks"""

if __name__ == '__main__':
    """Initialize a git repository based on the configured branch and repo"""
    url    = 'git@github.com:{{ cookiecutter.username }}/{{ cookiecutter.repo_name }}'
    branch = '{{ cookiecutter.branch }}'
    remote = '{{ cookiecutter.remote }}'
    gtest_link = 'git@github.com:google/googletest.git'
    gtest_path = 'external/GTest'
    
    import subprocess
    
    subprocess.call(('git', 'init'))
    subprocess.call(('git', 'checkout', '-b', branch))
    subprocess.call(('git', 'remote', 'add', remote, url))
    subprocess.call(('git', 'submodule', 'add', '--name', 'GTest', '--force', gtest_link, gtest_path))
    subprocess.call(('mv', 'pre-commit', '.git/hooks/'))
    
