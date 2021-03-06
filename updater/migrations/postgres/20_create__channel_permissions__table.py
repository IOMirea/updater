"""
IOMirea-server - A server for IOMirea messenger
Copyright (C) 2019  Eugene Ershov

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from migration import PGMigration


class Migration(PGMigration):
    async def up(self, latest: int) -> None:
        await self.conn.execute(
            """
            CREATE TABLE channel_permissions (
                user_id BIGINT NOT NULL,
                channel_id BIGINT NOT NULL,
                permissions BIT VARYING NOT NULL DEFAULT 0::bit,

                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
                FOREIGN KEY (channel_id) REFERENCES channels(id) ON DELETE CASCADE
            );

            DO
            $do$
            DECLARE
                user_id    BIGINT;
                channel_id BIGINT;
                channels   BIGINT[];
            BEGIN


                FOR user_id, channels IN
                    SELECT id, channel_ids FROM users
                LOOP
                    FOREACH channel_id IN ARRAY channels LOOP
                        INSERT INTO channel_permissions (user_id, channel_id)
                        VALUES (user_id, channel_id);
                    END LOOP;
                END LOOP;
            END
            $do$;
            """
        )
