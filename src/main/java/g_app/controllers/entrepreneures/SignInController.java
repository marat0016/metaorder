package g_app.controllers.entrepreneures;

import com.sun.org.apache.xpath.internal.operations.Bool;
import g_app.dao.UserDao;
import g_app.model.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.util.Assert;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Controller
public class SignInController {
    public static final String USERNAME_COOKIE_KEY = "username";
    UserDao userDao;

    @GetMapping("/sign-in-entrepreneur")
    public String signInForm(@CookieValue(value = USERNAME_COOKIE_KEY, defaultValue = "") String username,
                             @RequestParam(value = "exit", defaultValue = "") String isExit,
                             Model model) {
        if (!isExit.equals("")) {
            model.addAttribute("exit_msg", "You are exit.");
        }
        if (username.isEmpty()) {
            model.addAttribute("user", new User());
            return "sign-in-entrepreneur";
        } else {
            return "redirect:/welcome";
        }
    }

    @PostMapping("/sign-in-entrepreneur")
    public String signInSubmit(HttpServletResponse response, @ModelAttribute User user, Model model) {
        if (user.getName().isEmpty() || user.getPassword().isEmpty()) {
            model.addAttribute("empty_user_data", "You need to enter login data.");
            return "sign-in-entrepreneur";
        }
        if (userDao.isAuthorised(user)) {
            response.addCookie(new Cookie(USERNAME_COOKIE_KEY, user.getName()));
            return "redirect:/welcome";
        } else {
            model.addAttribute("invalid_user_data", "Invalid username or password.");
            return "sign-in-entrepreneur";
        }
    }

    @Autowired
    public void setUserDao(UserDao userDao) {
        Assert.notNull(userDao);
        this.userDao = userDao;
    }
}
