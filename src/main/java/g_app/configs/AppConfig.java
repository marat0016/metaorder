package g_app.configs;

import javax.sql.DataSource;
import g_app.controllers.entrepreneures.SignInController;
import g_app.controllers.entrepreneures.SignUpController;
import g_app.dao.UserDaoImpl;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.jdbc.core.namedparam.NamedParameterJdbcTemplate;
import org.springframework.jdbc.datasource.embedded.EmbeddedDatabaseBuilder;
import org.springframework.jdbc.datasource.embedded.EmbeddedDatabaseType;
import g_app.dao.UserDao;

@Configuration
@ComponentScan
public class AppConfig {

	@Bean
	public DataSource dataSource() {
		EmbeddedDatabaseBuilder builder = new EmbeddedDatabaseBuilder();
		builder.setType(EmbeddedDatabaseType.HSQL)
            .addScript("classpath:sql/create-db.sql")
            .addScript("classpath:sql/insert-data.sql");
		return builder.build();
	}

    @Bean
	public UserDao userDao() {
        return new UserDaoImpl(namedParamJdbcTemplate());
	}

	@Bean
	public SignInController signInController() {
		SignInController sic = new SignInController();
		sic.setUserDao(userDao());
		return sic;
	}

	@Bean
	public SignUpController signUpController() {
		SignUpController suc = new SignUpController();
		suc.setUserDao(userDao());
		return suc;
	}

	@Bean
	public NamedParameterJdbcTemplate namedParamJdbcTemplate() {
        return new NamedParameterJdbcTemplate(dataSource());
	}
} 