package g_app;

import g_app.dao.IUserDao;
import g_app.model.User;
import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
import org.springframework.transaction.annotation.Transactional;

@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(classes = { g_app.configs.AppConfig.class })
public class IUserDaoTest {

    public g_app.dao.IUserDao getUserDao() {
        return userDao;
    }

    public void setUserDao(g_app.dao.IUserDao userDao) {
        this.userDao = userDao;
    }

    @Autowired
    IUserDao userDao;

	String testName = "test";
	String testPassword = "test";

    @Before
    public void setUp() {
    }

    // todo: move to injection
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

    @After
    public void tearDown() {
    }

}