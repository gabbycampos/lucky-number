function snakeToCamel(s) {
    // uppercase letters after underscore
    // replace underscores with no space
    let result = '';
    for (let i=0; i < s.length; i++) {
        if (s[i-1] === '_') {
            result += s[i].toUpperCase();
        }
        else {
            result += s[i]
        }
    }
    return result.replace(/['_']/g, '');
}


