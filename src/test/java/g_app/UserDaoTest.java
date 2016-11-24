package g_app;

import g_app.dao.UserDaoImpl;
import g_app.model.User;
import g_app.dao.UserDao;
import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.jdbc.core.namedparam.NamedParameterJdbcTemplate;
import org.springframework.jdbc.datasource.embedded.EmbeddedDatabase;
import org.springframework.jdbc.datasource.embedded.EmbeddedDatabaseBuilder;
import org.springframework.jdbc.datasource.embedded.EmbeddedDatabaseType;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
import org.springframework.test.context.junit4.SpringRunner;

@ContextConfiguration(classes = { g_app.configs.AppConfig.class })
@RunWith(SpringJUnit4ClassRunner.class)
public class UserDaoTest {

	public void setUserDao(UserDao userDao) {
		this.userDao = userDao;
	}

	@Autowired
    UserDao userDao;

	String testName = "test";
	String testPassword = "test";


    @Test
    public void testFindByname() {
    	boolean	isRegistred = userDao.isUserRegistered(testName);
		User user = new User();
		user.setName(testName);
		user.setPassword(testPassword);
    	boolean	isAuthorized = userDao.isAuthorised(user);

    	Assert.assertEquals(true, isRegistred);
    	Assert.assertEquals(true, isAuthorized);
    }


}