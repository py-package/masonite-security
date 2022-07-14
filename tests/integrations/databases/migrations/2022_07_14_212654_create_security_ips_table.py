"""CreateSecurityIpsTable Migration."""

from masoniteorm.migrations import Migration


class CreateSecurityIpsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("security_ips") as table:
            table.increments("id")
            table.string("ip").index()
            table.boolean("blocked").default(True)
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("security_ips")
