#!/bin/sh

mongo localhost:27017/news <<-EOF
    rs.initiate({
        _id: "rs0",
        members: [ { _id: 0, host: getHostName() + ":27017" } ]
    });
EOF
echo "Initiated replica set"

sleep 5


mongo localhost:27017/admin <<-EOF
    db.createUser({ user: 'admin', pwd: 'admin', roles: [ { role: "userAdminAnyDatabase", db: "admin" } ] });
    db.grantRolesToUser("admin", ["clusterManager"]);
EOF

mongo -u admin -p admin localhost:27017/admin <<-EOF
    db.runCommand({
        createRole: "listDatabases",
        privileges: [
            { resource: { cluster : true }, actions: ["listDatabases"]}
        ],
        roles: []
    });
    db.createUser({
        user: 'rss_news',
        pwd: 'rss_news',
        roles: [
            { role: "readWrite", db: "rss_news" },
            { role: "read", db: "local" },
            { role: "listDatabases", db: "admin" },
            { role: "read", db: "config" },
            { role: "read", db: "admin" }
        ]
    });
EOF

