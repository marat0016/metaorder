package g_app.dao;

import g_app.model.User;
import org.hibernate.Criteria;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.criterion.Restrictions;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.orm.hibernate4.HibernateTemplate;
import org.springframework.stereotype.Repository;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.util.Assert;


public class UserDao implements IUserDao {
    private static final Logger log = LoggerFactory.getLogger(UserDao.class);

    @Autowired
    private SessionFactory sessionFactory;


    public void setSessionFactory(SessionFactory sf) {
        Assert.notNull(sf);
        this.sessionFactory = sf;
    }

    public Boolean isAuthorised(User user) {
        Session s = sessionFactory.getCurrentSession();
        Boolean isInDb = s.contains(user);
        return isInDb;
    }

    public Boolean isUserRegistered(String username) {
        Assert.notNull(username);
        Session s = sessionFactory.getCurrentSession();
        s.beginTransaction();
        Criteria criteria = s.createCriteria(User.class);
        User user = (User) criteria.add(Restrictions.eq("name", username)).uniqueResult();
        s.getTransaction().commit();
        return user != null;
    }

    public void createUser(User user) {
        Session s = sessionFactory.getCurrentSession();
        s.beginTransaction();
        s.persist(user);
        s.getTransaction().commit();
        log.info("User added successfully, Details = " + user);
    }
}
