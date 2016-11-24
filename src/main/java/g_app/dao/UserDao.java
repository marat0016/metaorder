package g_app.dao;


import g_app.model.User;

public interface UserDao {

    Boolean isAuthorised(User user);

    Boolean isUserRegistered(String username);

    void createUser(User user);
}
