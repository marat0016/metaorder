package g_app;

import ch.qos.logback.classic.LoggerContext;
import org.slf4j.LoggerFactory;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.builder.SpringApplicationBuilder;
import org.springframework.boot.web.support.SpringBootServletInitializer;

import java.util.Map;

@SpringBootApplication
public class Main extends SpringBootServletInitializer {

    @Override
    protected SpringApplicationBuilder configure(SpringApplicationBuilder application) {
        /*Map<String, String> vars = System.getenv();
        if (!vars.containsKey("catalina.base") && !vars.containsKey("catalina_base")) {
            LoggerContext context = (LoggerContext) LoggerFactory.getILoggerFactory();
            context.putProperty("LOGS_HOME", System.getProperty("user.dir"));
        }*/
        return application.sources(Main.class);
    }

    public static void main(String[] args) throws Exception {
        SpringApplication.run(Main.class, args);
    }

}
