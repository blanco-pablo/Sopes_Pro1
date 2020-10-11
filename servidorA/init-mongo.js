db.createUser(
    {
        user : "pablo",
        pwd : "12345678",
        roles: [
            {
                role: "readWrite",
                db : "db"
            }
        ]
    }
)