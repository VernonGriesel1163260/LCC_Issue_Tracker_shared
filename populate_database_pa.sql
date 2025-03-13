-- -----------------------------------------------------
-- Schema LCC_Issue_Tracker_db
-- -----------------------------------------------------
USE `VernonGriesel116$LCC_Issue_Tracker_db`;

-- Insert Users; Data is AI generated (except hashes), Script NOT
INSERT INTO `users` (`username`, `email`, `password_hash`, `first_name`, `last_name`, `location`, `role`, `profile_image`, `status`)
VALUES

    ('sthompson', 'sarah.t@example.com', '$2b$12$4z9sAt4d.WDCVv5mDciMXOOXSNMK9a8hwTm1Vu2kydXifudm3cU5K', 'Sarah', 'Thompson', 'Christchurch, Canterbury', 'visitor', 'default.png', 'active'),
    ('jwilson', 'james.w@example.com', '$2b$12$Ocae3BJyzT4Ww0gQO94aW.XsDAULhinBGMa2YqPOT800lldukCvfu', 'James', 'Wilson', 'Dunedin', 'visitor', 'default.png', 'active'),
    ('mchen', 'mei.c@example.com', '$2b$12$wDYAZSFD89zIQ8vuHJJBZ.PoTdSkDl75lRSZNMVpJAwI7W/G1RrV.', 'Mei', 'Chen', 'Auckland', 'visitor', 'default.png', 'active'),
    ('doconnor', 'david.o@example.com', '$2b$12$DR6C23iJVdtohbJJeceypOLbZoOyOQX2tLMEgOv/pwiq2Xh7v1T0q', 'David', 'O''Connor', 'Wellington', 'visitor', 'default.png', 'active'),
    ('aparker', 'amelia.p@example.com', '$2b$12$dXin8dQEoVP8HEI1LxW1w.9VzFHqSjBsN8epzFl7qKyMIyetdDfrK', 'Amelia', 'Parker', 'Lincoln, Canterbury', 'visitor', 'default.png', 'active'),
    ('rpatel', 'raj.p@example.com', '$2b$12$9Kn1Mvl2DWSiNPorUs30IezeL0HLCILVrp2VcDjc0AVR8yYbuZrXy', 'Raj', 'Patel', 'Hamilton', 'visitor', 'default.png', 'active'),
    ('efoster', 'emily.f@exampluserse.com', '$2b$12$Od9cA/T6DcKER4TaMcAWwOkv3SP1YkwtGqp//KDyYNe98mHf5IBOe', 'Emily', 'Foster', 'Queenstown', 'visitor', 'default.png', 'active'),
    ('mwilliams', 'michael.w@example.com', '$2b$12$Ge2ccM0Rb3MalFpD9dyxVeMlxHIyLa4YO.o9G4jAdMQLTrUcF/xwm', 'Michael', 'Williams', 'Timaru', 'visitor', 'default.png', 'active'),
    ('lsmith', 'lucy.s@example.com', '$2b$12$hU8JEYSlU81KhLRdv2VdueQbN5fX3Wp9EBK9RMMbpWNPrgwjhJZ0a', 'Lucy', 'Smith', 'Nelson', 'visitor', 'default.png', 'active'),
    ('btaylor', 'ben.t@example.com', '$2b$12$THSe6diGaraegIZLzYdCSO12GmjJY0ewkNqFKFGXUUE1jhqF.tw5G', 'Benjamin', 'Taylor', 'Tauranga', 'visitor', 'default.png', 'active'),
    ('alee', 'anna.l@example.com', '$2b$12$zfjozBUzPliiIO2uGOiMLe6ONpvoXiF5Tjn5.zuwgF6imCl1t1EYS', 'Anna', 'Lee', 'Rotorua', 'visitor', 'default.png', 'active'),
    ('jbrown', 'jack.b@example.com', '$2b$12$KCYvc6VEBXFNPCel0fqqpuuPBq.4TwsKVpC40GRUCaHHDzxm4Cr12', 'Jack', 'Brown', 'Napier', 'visitor', 'default.png', 'active'),
    ('kwood', 'kelly.w@example.com', '$2b$12$p6R1OqitEHhyGrjwm/Ty4ePuUm7c0F9QsYsDLAaqM37Zb6ZK0..7G', 'Kelly', 'Wood', 'Palmerston North', 'visitor', 'default.png', 'active'),
    ('dharris', 'daniel.h@example.com', '$2b$12$1V2kC1aaT1CwV752uM7kw.6G3af.Y65soH8lIXJwx3AEpR.6KHvGO', 'Daniel', 'Harris', 'Whangarei', 'visitor', 'default.png', 'active'),
    ('sclark', 'sophia.c@example.com', '$2b$12$wQpSOXuE/Rsa7S50CN6aze.pUReApguuC50.cbwHRMGDlYjJNmk9i', 'Sophia', 'Clark', 'Invercargill', 'visitor', 'default.png', 'active'),
    ('pnguyen', 'peter.n@example.com', '$2b$12$ptjILOE25oJBxgQIAfM3aekNyPwdRVWulqe1AKhUTrb7PgaDUErhm', 'Peter', 'Nguyen', 'Lower Hutt', 'visitor', 'default.png', 'active'),
    ('ywood', 'yasmin.w@example.com', '$2b$12$Nzik9V6Yh8O5v1WoFk.j/.YpbSytRj0ul/MBGKaGtFZYaasLE7M8G', 'Yasmin', 'Wood', 'Gisborne', 'visitor', 'default.png', 'active'),
    ('gking', 'george.k@example.com', '$2b$12$rxc.ReiLO5WZ31w4FivF2ujdxgMl/N4bhPObHUCUNnhnqKzv6MPi6', 'George', 'King', 'Blenheim', 'visitor', 'default.png', 'active'),
    ('ewhite', 'emma.w@example.com', '$2b$12$GhGTtrDlMfOgOlhcMt.NHeNvopMvWUb6D5LpSNXSzjSn3DNdfVYiy', 'Emma', 'White', 'Ashburton', 'visitor', 'default.png', 'active'),
    ('rjones', 'ryan.j@example.com', '$2b$12$LrYxZNj3P8b/plmhG4PFXeS/yCCBJjxz6GrLyIcfZdnLXHUrN7Gcu', 'Ryan', 'Jones', 'Rangiora', 'visitor', 'default.png', 'active'),
    ('janderson', 'john.a@example.com', '$2b$12$Bieue7Yho.hj0fgq5.Zu4ORm2VIbZMfUNjYOELacDc66uUdi5niV.', 'John', 'Anderson', 'Lincoln, Canterbury', 'helper', 'default.png', 'active'),
    ('mrodriguez', 'maria.r@example.com', '$2b$12$6yHHt64C5QYG2Xl0Swn12.HpNIDu08Z9OcXbexgfZClIje661SQHa', 'Maria', 'Rodriguez', 'Rolleston', 'helper', 'default.png', 'active'),
    ('tmitchell', 'thomas.m@example.com', '$2b$12$S64CMVxDAq6zDroKCXMPe.SeV559tQmElAOPf0ZhbG5XfXYE3YFna', 'Thomas', 'Mitchell', 'Lincoln, Canterbury', 'helper', 'default.png', 'active'),
    ('hstewart', 'hannah.s@example.com', '$2b$12$Oo5kPoD1unOuddkE61hWMeUBErr.kVgspRN9L.WCZW.TXd3U/NhAC', 'Hannah', 'Stewart', 'Prebbleton', 'helper', 'default.png', 'active'),
    ('wturner', 'william.t@example.com', '$2b$12$WO9Y5X14dt9j5PoKpCSnEuwBbo55hXZuH0PAN.dWPfk7h63BhHb6m', 'William', 'Turner', 'Tai Tapu', 'helper', 'default.png', 'active'),
    ('mcollins', 'margaret.c@example.com', '$2b$12$pwi6CGOJ27D0C3RNzL0Fsed5M4EbR6T9bqDApdDzOQETPge7H67E.', 'Margaret', 'Collins', 'Lincoln, Canterbury', 'admin', 'default.png', 'active'),
    ('rclarke', 'robert.c@example.com', '$2b$12$5F75D4d3qW1hYmmVSsgobeA.mr8eBwDzAyVJZvDH0Twf0qc7HMkfe', 'Robert', 'Clarke', 'Springston', 'admin', 'default.png', 'active')
;

-- Insert Issues; Data is AI generated, Script NOT
INSERT INTO `issues` (`user_id`, `summary`, `description`, `status`, `created_at`)
VALUES
    -- Issue 1: WiFi Problem (Reported by Sarah Thompson)
    ((SELECT user_id FROM users WHERE username = 'sthompson'),
    'WiFi not working in north camping area',
    'Unable to connect to the campground WiFi from sites 15-20. The signal shows full strength but cannot establish connection.',
    'open',
    '2025-02-15 09:30:00'),

    -- Issue 2: Blocked Toilet (Reported by Raj Patel)
    ((SELECT user_id FROM users WHERE username = 'rpatel'),
    'Blocked toilet in main facilities block',
    'The middle toilet in the mens section of the main facilities block appears to be blocked. Water rises but drains very slowly.',
    'resolved',
    '2025-02-18 15:45:00'),

    -- Issue 3: Damaged Fire Pit (Reported by Mei Chen)
    ((SELECT user_id FROM users WHERE username = 'mchen'),
    'Fire pit damaged at site 7',
    'The stone ring around the fire pit at site 7 has several loose rocks. Some appear to have been removed. Could be dangerous if used in current state.',
    'stalled',
    '2025-02-20 17:15:00'),

    -- Issue 4: Charging station not working (Reported by Lucy Smith)
    ((SELECT user_id FROM users WHERE username = 'lsmith'),
    'Charging station not working',
    'Solar charging station near site 12 isn''t powering up. Green light not showing.',
    'new',
    '2025-02-21 10:00:00'),

    -- Issue 5: Water pressure (Reported by Benjamin Taylor)
    ((SELECT user_id FROM users WHERE username = 'btaylor'),
    'Water pressure low in showers',
    'Very low water pressure in all shower cubicles this morning.',
    'open',
    '2025-02-21 08:15:00'),

    -- Issue 6: Fallen tree branch (Reported by Anna Lee)
    ((SELECT user_id FROM users WHERE username = 'alee'),
    'Fallen tree branch near site 9',
    'Large branch came down in last night''s wind, blocking access to site 9.',
    'resolved',
    '2025-02-20 07:30:00'),

    -- Issue 7: BBQ gas bottle empty (Reported by Jack Brown)
    ((SELECT user_id FROM users WHERE username = 'jbrown'),
    'BBQ gas bottle empty',
    'Main BBQ area gas bottle appears to be empty, no flame when trying to light.',
    'resolved',
    '2025-02-19 18:45:00'),

    -- Issue 8: Rubbish bin overflowing (Reported by Kelly Wood)
    ((SELECT user_id FROM users WHERE username = 'kwood'),
    'Rubbish bin overflowing',
    'Main rubbish collection point is overflowing, attracting birds.',
    'resolved',
    '2025-02-19 16:20:00'),

    -- Issue 9: Site marker missing (Reported by Daniel Harris)
    ((SELECT user_id FROM users WHERE username = 'dharris'),
    'Site marker missing',
    'Site number marker for site 14 has fallen off the post.',
    'new',
    '2025-02-21 11:30:00'),

    -- Issue 10: Light out in toilet block (Reported by Sophia Clark)
    ((SELECT user_id FROM users WHERE username = 'sclark'),
    'Light out in toilet block',
    'Main light in women''s toilet block not working.',
    'open',
    '2025-02-21 05:45:00'),

    -- Issue 11: Water tap leaking (Reported by Peter Nguyen)
    ((SELECT user_id FROM users WHERE username = 'pnguyen'),
    'Water tap leaking',
    'Drinking water tap near site 5 is dripping constantly.',
    'new',
    '2025-02-21 14:00:00'),

    -- Issue 12: Picnic table damaged (Reported by Yasmin Wood)
    ((SELECT user_id FROM users WHERE username = 'ywood'),
    'Picnic table damaged',
    'Loose board on picnic table at site 11, screw needs tightening.',
    'new',
    '2025-02-21 13:15:00'),

    -- Issue 13: Spider web in shower (Reported by George King)
    ((SELECT user_id FROM users WHERE username = 'gking'),
    'Spider web in shower',
    'Large spider web in shower cubicle 3, spider present.',
    'resolved',
    '2025-02-19 07:30:00'),

    -- Issue 14: Gate not closing properly (Reported by Emma White)
    ((SELECT user_id FROM users WHERE username = 'ewhite'),
    'Gate not closing properly',
    'Main entrance gate not closing automatically as it should.',
    'stalled',
    '2025-02-20 16:45:00'),

    -- Issue 15: Noisy generator (Reported by Ryan Jones)
    ((SELECT user_id FROM users WHERE username = 'rjones'),
    'Noisy generator at site 16',
    'Camper at site 16 running generator outside quiet hours (after 10pm).',
    'resolved',
    '2025-02-19 22:30:00'),

    -- Issue 16: Missing recycling bin (Reported by Michael Williams)
    ((SELECT user_id FROM users WHERE username = 'mwilliams'),
    'Missing recycling bin',
    'Glass recycling bin seems to have disappeared from main collection point.',
    'open',
    '2025-02-21 09:45:00'),

    -- Issue 17: Power outlet not working (Reported by Emily Foster)
    ((SELECT user_id FROM users WHERE username = 'efoster'),
    'Power outlet not working',
    'Power outlet at site 3 showing no power, checked RCD switch.',
    'new',
    '2025-02-21 15:30:00'),

    -- Issue 18: Wasps nest found (Reported by Amelia Parker)
    ((SELECT user_id FROM users WHERE username = 'aparker'),
    'Wasps nest found',
    'Active wasps nest discovered in tree near site 8.',
    'open',
    '2025-02-21 12:00:00'),

    -- Issue 19: Broken picnic shelter (Reported by David O''Connor)
    ((SELECT user_id FROM users WHERE username = 'doconnor'),
    'Broken picnic shelter',
    'The picnic shelter near the main lawn has broken supports and is unsafe for use.',
    'new',
    '2025-02-21 13:45:00'),

    -- Issue 20: Damaged signage (Reported by James Wilson)
    ((SELECT user_id FROM users WHERE username = 'jwilson'),
    'Damaged signage at entrance',
    'The sign at the main entrance is partially damaged and difficult to read.',
    'open',
    '2025-02-21 14:30:00')
;

-- Insert Comments ; Data is AI generated, Script NOT
INSERT INTO `comments` (`issue_id`, `user_id`, `content`, `created_at`)
VALUES
    -- Comments on WiFi
    (1, (SELECT user_id FROM users WHERE username = 'janderson'),
    'Thanks for reporting this. I''ll check the router settings and signal boosters in that area today.',
    '2025-02-15 10:15:00'),

    (1, (SELECT user_id FROM users WHERE username = 'sthompson'),
    'Thank you. The issue seems intermittent - sometimes it connects briefly before dropping out again.',
    '2025-02-15 11:30:00'),

    (1, (SELECT user_id FROM users WHERE username = 'janderson'),
    'Found the problem - one of the signal repeaters needs replacement. Parts ordered, should arrive in 2-3 days.',
    '2025-02-15 14:45:00'),

    -- Comments on Blocked Toilet
    (2, (SELECT user_id FROM users WHERE username = 'tmitchell'),
    'I''ll take a look at this right away with the plunger.',
    '2025-02-18 16:00:00'),

    (2, (SELECT user_id FROM users WHERE username = 'tmitchell'),
    'Issue has been resolved. Cleared the blockage and tested - all working normally now.',
    '2025-02-18 16:30:00'),

    (2, (SELECT user_id FROM users WHERE username = 'rpatel'),
    'Confirmed working properly now. Thanks for the quick response!',
    '2025-02-18 17:00:00'),

    -- Comments on Fire Pit
    (3, (SELECT user_id FROM users WHERE username = 'mrodriguez'),
    'I''ve inspected the fire pit and marked it as unsafe. Will need to source matching stones for repair.',
    '2025-02-20 18:00:00'),

    (3, (SELECT user_id FROM users WHERE username = 'mcollins'),
    'Put up temporary barriers and "Do Not Use" sign. Our stone supplier is currently out of stock of matching rocks. Will update once we have an ETA.',
    '2025-02-21 09:00:00'),

    (3, (SELECT user_id FROM users WHERE username = 'mchen'),
    'Thanks for the quick response and safety measures.',
    '2025-02-21 10:15:00'),

    -- Comment on Charging Station
    (4, (SELECT user_id FROM users WHERE username = 'tmitchell'),
    'Checking the solar panels now; seems like a hardware fault.',
    '2025-02-21 10:30:00'),

    -- Comment on Water Pressure
    (5, (SELECT user_id FROM users WHERE username = 'wturner'),
    'I''ll inspect the water supply line to see if a valve is partially closed.',
    '2025-02-21 08:45:00'),

    -- Comment on Fallen Tree Branch
    (6, (SELECT user_id FROM users WHERE username = 'tmitchell'),
    'Cleared the branch from the pathway. Safety sign will be added.',
    '2025-02-20 08:00:00'),

    -- Comment on BBQ Gas Bottle
    (7, (SELECT user_id FROM users WHERE username = 'mrodriguez'),
    'Replaced the gas bottle and tested the grill. It''s working now.',
    '2025-02-19 19:15:00'),

    -- Comment on Site Marker
    (9, (SELECT user_id FROM users WHERE username = 'wturner'),
    'Reattached the site marker after finding a loose bolt.',
    '2025-02-21 12:00:00'),

    -- Comment on Light in Toilet Block
    (10, (SELECT user_id FROM users WHERE username = 'tmitchell'),
    'Ordered a new light bulb for the block; technician scheduled for tomorrow.',
    '2025-02-21 06:15:00'),

    -- Comment on Water Tap Leaking
    (11, (SELECT user_id FROM users WHERE username = 'janderson'),
    'Noticed the leak; will repair the tap fittings shortly.',
    '2025-02-21 14:15:00'),

    -- Comment on Picnic Table Damaged
    (12, (SELECT user_id FROM users WHERE username = 'janderson'),
    'Tightened the loose screw; table is now stable.',
    '2025-02-21 13:45:00'),

    -- Comment on Spider Web in Shower
    (13, (SELECT user_id FROM users WHERE username = 'mcollins'),
    'Removed the spider web and cleaned the shower area.',
    '2025-02-19 08:00:00'),

    -- Comment on Gate
    (14, (SELECT user_id FROM users WHERE username = 'tmitchell'),
    'Adjusted the gate mechanism; it should close properly now.',
    '2025-02-20 17:00:00'),

    -- Comment on Noisy Generator
    (15, (SELECT user_id FROM users WHERE username = 'mrodriguez'),
    'Advised the camper to reduce noise; generator settings adjusted.',
    '2025-02-19 23:00:00'),

    -- Comment on Missing Recycling Bin
    (16, (SELECT user_id FROM users WHERE username = 'janderson'),
    'Reported to waste management; a new bin will be delivered soon.',
    '2025-02-21 10:00:00'),

    -- Comment on Power Outlet
    (17, (SELECT user_id FROM users WHERE username = 'hstewart'),
    'Investigating the circuit breaker; might need an electrician.',
    '2025-02-21 16:00:00'),

    -- Comment on Wasps Nest
    (18, (SELECT user_id FROM users WHERE username = 'tmitchell'),
    'Called pest control; nest will be removed safely.',
    '2025-02-21 12:30:00'),

    -- Comment on Broken Picnic Shelter
    (19, (SELECT user_id FROM users WHERE username = 'mcollins'),
    'Scheduled repair work for the picnic shelter; temporary sign posted.',
    '2025-02-21 14:00:00'),

    -- Comment on Damaged Signage
    (20, (SELECT user_id FROM users WHERE username = 'tmitchell'),
    'Ordering a new sign; will install as soon as it arrives.',
    '2025-02-21 15:00:00')
;