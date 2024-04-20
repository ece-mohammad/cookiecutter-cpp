#include <gtest/gtest.h>
#include <{{cookiecutter.repo_name.lower()}}.hpp>

TEST({{ cookiecutter.project_name | capitalize }}Test, Contrived) {
    EXPECT_TRUE(true);
}
