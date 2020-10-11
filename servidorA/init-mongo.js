db.createUser(
    {
        user : "pablo",
        pwd : "root",
        roles: [
            {
                role: "readWrite",
                db : "mydb"
            }
        ]
    }
)