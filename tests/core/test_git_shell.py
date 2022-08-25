from ggshield.core.git_shell import GIT_PATH, is_git_dir, is_valid_git_commit_ref, shell


def test_git_shell():
    assert "usage: git" in shell([GIT_PATH, "help"])


def test_is_git_dir():
    assert is_git_dir()


def test_is_valid_git_commit_ref():
    assert is_valid_git_commit_ref("HEAD")
    assert not is_valid_git_commit_ref("invalid_ref")
