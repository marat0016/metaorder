package g_app.dao;

import g_app.model.User;
import org.springframework.transaction.annotation.Propagation;
import org.springframework.transaction.annotation.Transactional;

// @Transactional(propagation = Propagation.REQUIRED)
public interface IUserDao {

    Boolean isAuthorised(User user);

    Boolean isUserRegistered(String username);

    void createUser(User user);
}
