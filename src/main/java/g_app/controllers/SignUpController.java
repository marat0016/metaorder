package g_app.controllers;

import g_app.dao.IUserDao;
import g_app.model.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.util.Assert;
import org.springframework.web.bind.annotation.CookieValue;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletResponse;

import java.util.HashMap;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import static g_app.controllers.SignInController.USERNAME_COOKIE_KEY;

@Controller
public class

SignUpController {
    IUserDao IUserDao;

    @GetMapping("/sign-up")
    public String registrationForm(@CookieValue(value = USERNAME_COOKIE_KEY, defaultValue = "") String username, Model model) {
        if (username.isEmpty()) {
            model.addAttribute("user", new User());
            return "sign-up";
        } else {
            return "redirect:/welcome";
        }
    }

    @PostMapping("/sign-up")
    public String registrationSubmit(HttpServletResponse response, @ModelAttribute User user, Model model) {
        Map<String, String> errors = new HashMap<>();
        if (isInvalidUsername(user.getName())) {
            errors.put("invalid_username", "Invalid username: must contains alphabetic characters, numbers and have size > 4");
        }
        if (isInvalidPassword(user.getPassword())) {
            errors.put("invalid_password", "Invalid password: must contains lower and upper case alphabetic characters, " +
                    "numbers and have size > 8");
        }
        if (errors.size() > 0) {
            model.addAllAttributes(errors);
            return "sign-up";
        }

        if (IUserDao.isUserRegistered(user.getName())) {
            model.addAttribute("name_busy", "User with this name is already registered");
            return "sign-up";
        } else {
            IUserDao.createUser(user);
            response.addCookie(new Cookie(USERNAME_COOKIE_KEY, user.getName()));
            return "redirect:/welcome";
        }
    }

    @Autowired
    public void setIUserDao(IUserDao IUserDao) {
        Assert.notNull(IUserDao);
        this.IUserDao = IUserDao;
    }

    private boolean isInvalidUsername(String username) {
        Pattern pattern = Pattern.compile("(?=(.*[0-9]))(?=.*[a-z])[0-9a-zA-Z]{4,}");
        Matcher matcher = pattern.matcher(username);
        return !matcher.matches();
    }

    private boolean isInvalidPassword(String password) {
        Pattern pattern = Pattern.compile("(?=(.*[0-9]))(?=.*[a-z])(?=(.*[A-Z]))[0-9a-zA-Z]{8,}");
        Matcher matcher = pattern.matcher(password);
        return !matcher.matches();
    }
}
