class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    if user in group.users:
        return True

    for subgroup in group.groups:
        return is_user_in_group(user, subgroup)

    return False


def test():

    # Create example
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")
    child_user = "child_user"
    child.add_user(child_user)
    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)
    child.add_group(sub_child)
    parent.add_group(child)

    # Test 1
    assert is_user_in_group(child_user, sub_child) == False
    assert is_user_in_group(child_user, child) == True
    assert is_user_in_group(child_user, parent) == True

    # Test 2
    assert is_user_in_group(sub_child_user, sub_child) == True
    assert is_user_in_group(sub_child_user, child) == True
    assert is_user_in_group(sub_child_user, parent) == True

    # Test 3
    assert is_user_in_group('new_group', parent) == False

    print("All tests successful")

if __name__ == '__main__':
    test()