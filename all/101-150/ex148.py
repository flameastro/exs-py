# ex148: Crie uma função que identifique as partes de um email e separe em Nome, Domínio e TLD
def mail_parts(mail: str):
    if mail.count("@") > 1 or mail.count(".") > 1:
        return "E-mail inválido."

    name = mail[:mail.index("@")]
    domain = mail[mail.index("@")+1:mail.index(".")]
    extension = mail[mail.index(".")+1:]

    return f"Nome: {name} | Domínio (Email): {domain} | Extensão (TLD/GTLD/CCTLD): {extension}"

if __name__ == "__main__":
    print(mail_parts("semprotecao123@gmail.com"))  # Nome: semprotecao123 | Domínio (Email): gmail | Extensão (TLD/GTLD/CCTLD): com
    print(mail_parts("anonymous@proton.me"))  # Nome: anonymous | Domínio (Email): proton | Extensão (TLD/GTLD/CCTLD): me
    print(mail_parts("fbi_acc@tutamail.com"))  # Nome: fbi_acc | Domínio (Email): tutamail | Extensão (TLD/GTLD/CCTLD): com
    print(mail_parts("none.anonymous@gmail.com"))  # E-mail inválido.

