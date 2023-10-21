
export function check_email(email) {
    // Функция валидации почты
    const domain = email.split('@')[1];
    const domain_templates = {
        email: 'mail.ru',
        gmail: 'gmail.com',
        yandex: 'yandex.ru'
    };

    if (email === '') {
        return false;
    }

    if (!~email.indexOf('@')) {
        return false;
    }

    for (const key in domain_templates) {
        const element = domain_templates[key];
        if (element === domain) {
            return true;
        }
    }

    return false;
}

export function check_password(password) {
    // Функция валидации пароля
    const min_len = 3;
    const max_len = 50;

    if (password === '') {
        return false;
    }
    if (password.length < min_len || password.length > max_len) {
        return false;
    }
    return true;
}

export function equals_password(password1, password2) {
    return password1 === password2 ? true : false
}