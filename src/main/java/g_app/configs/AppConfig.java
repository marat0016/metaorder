package g_app.configs;

import javax.sql.DataSource;

import g_app.controllers.SignInController;
import g_app.controllers.SignUpController;
import org.apache.commons.dbcp.BasicDataSource;
import org.hibernate.SessionFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.orm.hibernate4.HibernateTemplate;
import org.springframework.orm.hibernate4.HibernateTransactionManager;
import org.springframework.orm.hibernate4.LocalSessionFactoryBuilder;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import g_app.dao.IUserDao;
import g_app.dao.UserDao;
import g_app.model.User;

import java.util.Properties;

@Configuration 
@EnableTransactionManagement
public class AppConfig {
    @Bean
	public IUserDao userDao() {
		UserDao ud = new UserDao();
		ud.setSessionFactory(sessionFactory());
		return ud;
	}

	@Bean
	public SignInController signInController() {
		SignInController sic = new SignInController();
		sic.setIUserDao(userDao());
		return sic;
	}

	@Bean
	public SignUpController signUpController() {
		SignUpController suc = new SignUpController();
		suc.setIUserDao(userDao());
		return suc;
	}

	@Bean
	public HibernateTemplate hibernateTemplate() {
		return new HibernateTemplate(sessionFactory());
	}

	@Bean
	public SessionFactory sessionFactory() {
		Properties props = new Properties();
		props.put("hibernate.dialect", "org.hibernate.dialect.PostgreSQLDialect");
		props.put("hibernate.current_session_context_class", "thread");
		props.put("hibernate.connection.url", "jdbc:postgresql://localhost:5432/metaorder");
		// props.put("hibernate.connection.provider_class", "org.hibernate.c3p0.connection.C3P0ConnectionProvider");

		SessionFactory sf = new LocalSessionFactoryBuilder(getDataSource())
				.addAnnotatedClasses(User.class)
				.setProperties(props)
				.buildSessionFactory();

		return sf;
	}

	@Bean
	public DataSource getDataSource() {
	    BasicDataSource dataSource = new BasicDataSource();
	    dataSource.setDriverClassName("org.postgresql.Driver");
	    dataSource.setUrl("jdbc:postgresql://localhost:5432/metaorder");
	    dataSource.setUsername("metaorder");
	    dataSource.setPassword("almar18");
	    return dataSource;
	}

	/*@Bean
	public HibernateTransactionManager transactionManager() {
		HibernateTransactionManager txManager = new HibernateTransactionManager();
		txManager.setSessionFactory(sessionFactory());
		return txManager;
	}*/

	/*@Bean
	public HibernateTransactionManager hibTransMan(){
		return new HibernateTransactionManager(sessionFactory());
	}*/
} 