package g_app.dao;

import g_app.model.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.jdbc.core.namedparam.NamedParameterJdbcTemplate;
import org.springframework.stereotype.Repository;
import org.springframework.util.Assert;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.HashMap;
import java.util.Map;

@Repository
public class UserDaoImpl implements UserDao {
    @Autowired
    NamedParameterJdbcTemplate namedParameterJdbcTemplate;

    public Boolean isAuthorised(User user) {
        Map<String, Object> params = new HashMap<String, Object>();
        params.put("name", user.getName());
        params.put("password", user.getPassword());

        String sql = "SELECT count(*) FROM Users WHERE name=:name AND password=:password";
        Integer num = namedParameterJdbcTemplate.queryForObject(sql, params, Integer.class);
        int count = (num != null ? num.intValue() : 0);
        Assert.isTrue(count < 2);

        return count > 0;
    }

    public Boolean isUserRegistered(String username) {
        Map<String, Object> params = new HashMap<String, Object>();
        params.put("name", username);

        String sql = "SELECT count(*) FROM Users WHERE name=:name";
        Integer num = namedParameterJdbcTemplate.queryForObject(sql, params, Integer.class);
        int count = (num != null ? num.intValue() : 0);
        Assert.isTrue(count < 2);

        return count > 0;
    }

    public void createUser(User user) {
        String insertTestValue = "INSERT INTO Users VALUES (:name, :password);";
        Map<String, Object> params = new HashMap<String, Object>();
        params.put("name", user.getName());
        params.put("password", user.getPassword());
        namedParameterJdbcTemplate.execute(insertTestValue, params, PreparedStatement::execute);
    }

    private static final class UserMapper implements RowMapper<User> {

        public User mapRow(ResultSet rs, int rowNum) throws SQLException {
            User user = new User();
            user.setName(rs.getString("name"));
            user.setPassword(rs.getString("password"));
            return user;
        }
    }

    public UserDaoImpl(NamedParameterJdbcTemplate jdbcTemplate) {
        Assert.notNull(jdbcTemplate, "JDBC Template cannot be null.");
        this.namedParameterJdbcTemplate = jdbcTemplate;
    }
}
