"""CreateSecurityLogsTable Migration."""

from masoniteorm.migrations import Migration


class CreateSecurityLogsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("security_logs") as table:
            table.increments("id")
            table.string("user_id").nullable()
            table.string("ip").index()
            table.string("url").nullable()
            table.string("method").nullable()
            table.string("user_agent").nullable()
            table.string("referrer").nullable()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("security_logs")
