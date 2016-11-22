package g_app.controllers;

import g_app.dao.IUserDao;
import g_app.model.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.util.Assert;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletResponse;

@Controller
public class SignInController {
    public static final String USERNAME_COOKIE_KEY = "username";
    IUserDao IUserDao;

//    private PhoneService phoneService;
//
//    @Autowired(required = true)
//    // @Qualifier(value = "phoneService")
//    public void setPhoneService(PhoneService ps) {
//        Assert.notNull(ps);
//        this.phoneService = ps;
//    }
//
//    @GetMapping("/s")
//    public String justPage(Model model) {
//        List<Phone> p = phoneService.listPhones();
//        Assert.isTrue(p.size() > 0);
//        model.addAttribute("phone", p.get(0));
//        return "phones";
//    }

    @GetMapping("/sign-in")
    public String signInForm(@CookieValue(value = USERNAME_COOKIE_KEY, defaultValue = "") String username,
                             @RequestParam(value = "exit", defaultValue = "") String isExit,
                             Model model) {
        if (!isExit.equals("")) {
            model.addAttribute("exit_msg", "You are exit.");
        }
        if (username.isEmpty()) {
            model.addAttribute("user", new User());
            return "sign-in";
        } else {
            return "redirect:/welcome";
        }
    }

    @PostMapping("/sign-in")
    public String signInSubmit(HttpServletResponse response, @ModelAttribute User user, Model model) {
        if (user.getName().isEmpty() || user.getPassword().isEmpty()) {
            model.addAttribute("empty_user_data", "You need to enter login data.");
            return "sign-in";
        }
        if (IUserDao.isAuthorised(user)) {
            response.addCookie(new Cookie(USERNAME_COOKIE_KEY, user.getName()));
            return "redirect:/welcome";
        } else {
            model.addAttribute("invalid_user_data", "Invalid username or password.");
            return "sign-in";
        }
    }

    @Autowired
    public void setIUserDao(IUserDao IUserDao) {
        Assert.notNull(IUserDao);
        this.IUserDao = IUserDao;
    }
}
