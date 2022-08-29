from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="basic_oxygen_furnace",
    accept_cargos_with_input_ratios=[
        ("IRON", 4),
        ("MNO2", 2),
        ("QLME", 1),
        ("O2__", 1),
    ],
    combined_cargos_boost_prod=True,
    prod_cargo_types_with_output_ratios=[("STCB", 4), ("STAL", 2), ("SLAG", 2)],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="49",
    special_flags=["IND_FLAG_MILITARY_HELICOPTER_CAN_EXPLODE"],
    location_checks=dict(
        near_at_least_one_of_these_keystone_industries=[["blast_furnace"], 72],
        same_type_distance=72,
    ),
    name="string(STR_IND_BASIC_OXYGEN_FURNACE)",
    nearby_station_name="string(STR_STATION_FURNACE)",
    fund_cost_multiplier="160",
    pollution_and_squalor_factor=2,
)

industry.economy_variations["STEELTOWN"].enabled = True
industry.economy_variations[
    "STEELTOWN"
].prob_in_game = "0"  # do not build during gameplay

industry.add_tile(
    id="basic_oxygen_furnace_tile_1",
    animation_length=7,
    animation_looping=True,
    animation_speed=3,
    custom_animation_control={
        "macro": "random_first_frame",
        "animation_triggers": "bitmask(ANIM_TRIGGER_INDTILE_CONSTRUCTION_STATE)",
    },
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)
industry.add_tile(
    id="basic_oxygen_furnace_tile_2",
    animation_length=30,
    animation_looping=True,
    animation_speed=4,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(
    type="hard_standing_dirt",
)
spriteset_ground_overlay = industry.add_spriteset(
    type="empty",
)
spriteset_tanks = industry.add_spriteset(
    sprites=[(150, 10, 64, 122, -31, -90)],
)
spriteset_furnace = industry.add_spriteset(
    sprites=[(220, 10, 64, 122, -31, -90)],
)
spriteset_air_plant = industry.add_spriteset(
    sprites=[(290, 10, 64, 122, -31, -90)],
)
spriteset_caster = industry.add_spriteset(
    sprites=[(360, 10, 64, 122, -31, -90)],
)
spriteset_metal_1 = industry.add_spriteset(
    sprites=[(430, 10, 64, 122, -31, -90)],
)
spriteset_metal_2 = industry.add_spriteset(
    sprites=[(500, 10, 64, 122, -31, -90)],
)
spriteset_metal_3 = industry.add_spriteset(
    sprites=[(570, 10, 64, 122, -31, -90)],
)
spriteset_metal_4 = industry.add_spriteset(
    sprites=[(640, 10, 64, 122, -31, -90)],
)
spriteset_shed = industry.add_spriteset(
    sprites=[(710, 10, 64, 122, -31, -90)],
)
spriteset_caster_crane_animated = industry.add_spriteset(
    sprites=[
        (10, 250, 64, 64, -31, -33),
        (80, 250, 64, 64, -31, -33),
        (150, 250, 64, 64, -31, -33),
        (220, 250, 64, 64, -31, -33),
        (290, 250, 64, 64, -31, -33),
        (360, 250, 64, 64, -31, -33),
        (430, 250, 64, 64, -31, -33),
        (500, 250, 64, 64, -31, -33),
        (570, 250, 64, 64, -31, -33),
        (640, 250, 64, 64, -31, -33),
    ],
    animation_rate=1,
    custom_sprite_selector="(animation_frame < 10) ? (animation_frame % 10) : 0",
)
spriteset_caster_gantry_animated = industry.add_spriteset(
    sprites=[
        (10, 160, 64, 64, -31, -33),
    ],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_caster_crane_animated.sprites),
)
spriteset_ground_tile_dark_animated = industry.add_spriteset(
    sprites=[(80, 10, 64, 122, -31, -91)],
    # autofills number of frames to match another spriteset which is animated etc (can get frame count from the other spriteset if defined already)
    num_sprites_to_autofill=len(spriteset_caster_crane_animated.sprites),
)
spriteset_caster_metal_run_animated = industry.add_spriteset(
    sprites=[
        (10, 340, 64, 64, -31, -33),
        (80, 340, 64, 64, -31, -33),
        (150, 340, 64, 64, -31, -33),
        (220, 340, 64, 64, -31, -33),
        (290, 340, 64, 64, -31, -33),
        (360, 340, 64, 64, -31, -33),
        (430, 340, 64, 64, -31, -33),
        (500, 340, 64, 64, -31, -33),
        (570, 340, 64, 64, -31, -33),
        (640, 340, 64, 64, -31, -33),
    ],
    animation_rate=1,
    custom_sprite_selector="(animation_frame < 10) ? (animation_frame % 10) : 0",
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=1,
    yoffset=0,
    zoffset=61,
)
sprite_smoke_2 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=4,
    yoffset=1,
    zoffset=93,
)

industry.add_spritelayout(
    id="basic_oxygen_furnace_spritelayout_empty",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="basic_oxygen_furnace_spritelayout_tanks",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_tanks],
    fences=[],
)
industry.add_spritelayout(
    id="basic_oxygen_furnace_spritelayout_air_plant",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_air_plant],
    smoke_sprites=[sprite_smoke_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="basic_oxygen_furnace_spritelayout_furnace",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_furnace],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="basic_oxygen_furnace_spritelayout_casting_shed",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_caster],
    smoke_sprites=[sprite_smoke_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="basic_oxygen_furnace_spritelayout_metal_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_metal_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="basic_oxygen_furnace_spritelayout_metal_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_metal_2],
    fences=[],
)
industry.add_spritelayout(
    id="basic_oxygen_furnace_spritelayout_metal_3",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_metal_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="basic_oxygen_furnace_spritelayout_metal_4",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_metal_4],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="basic_oxygen_furnace_spritelayout_small_shed",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_shed],
    fences=["nw", "se"],
)
industry.add_spritelayout(
    id="basic_oxygen_furnace_spritelayout_animated_ladle_front_part",
    ground_sprite=spriteset_ground_tile_dark_animated,
    ground_overlay=spriteset_ground_tile_dark_animated,
    building_sprites=[
        spriteset_caster_gantry_animated,
        spriteset_caster_crane_animated,
    ],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="basic_oxygen_furnace_spritelayout_animated_ladle_rear_part",
    ground_sprite=spriteset_ground_tile_dark_animated,
    ground_overlay=spriteset_ground_tile_dark_animated,
    building_sprites=[spriteset_caster_metal_run_animated],
    fences=["nw", "ne", "se", "sw"],
)

# this industry needs outpost layout as there are lots of cargos
industry.add_industry_outpost_layout(
    id="basic_oxygen_furnace_industry_outpost_layout_1",
    layout=[
        # test outpost layout
        (
            0,
            0,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            0,
            1,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_air_plant",
        ),
        (
            1,
            0,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            1,
            1,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_tanks",
        ),
        (
            2,
            0,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_metal_1",
        ),
        (
            2,
            1,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_small_shed",
        ),
    ],
)
# core layouts are roughly 6x4 or 5x5
industry.add_industry_layout(
    id="basic_oxygen_furnace_industry_layout_1",
    layout=[
        (
            0,
            0,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            0,
            1,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            0,
            2,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            0,
            3,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            0,
            4,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_air_plant",
        ),
        (
            1,
            0,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            1,
            1,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            1,
            2,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            1,
            3,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            1,
            4,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_tanks",
        ),
        (
            2,
            0,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            2,
            1,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            2,
            2,
            "basic_oxygen_furnace_tile_2",
            "basic_oxygen_furnace_spritelayout_animated_ladle_rear_part",
        ),
        (
            2,
            3,
            "basic_oxygen_furnace_tile_2",
            "basic_oxygen_furnace_spritelayout_animated_ladle_front_part",
        ),
        (
            2,
            4,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_small_shed",
        ),
    ],
)
industry.add_industry_layout(
    id="basic_oxygen_furnace_industry_layout_2",
    layout=[
        (
            0,
            0,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            0,
            1,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            0,
            2,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            0,
            3,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            0,
            4,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            1,
            0,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            1,
            1,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            1,
            2,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            1,
            3,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            1,
            4,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_metal_1",
        ),
        (
            2,
            0,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_air_plant",
        ),
        (
            2,
            1,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            2,
            2,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            2,
            3,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            2,
            4,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_air_plant",
        ),
        (
            3,
            0,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_tanks",
        ),
        (
            3,
            1,
            "basic_oxygen_furnace_tile_2",
            "basic_oxygen_furnace_spritelayout_small_shed",
        ),
        (
            3,
            2,
            "basic_oxygen_furnace_tile_2",
            "basic_oxygen_furnace_spritelayout_animated_ladle_rear_part",
        ),
        (
            3,
            3,
            "basic_oxygen_furnace_tile_2",
            "basic_oxygen_furnace_spritelayout_animated_ladle_front_part",
        ),
        (
            3,
            4,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_tanks",
        ),
    ],
)
industry.add_industry_layout(
    id="basic_oxygen_furnace_industry_layout_3",
    layout=[
        (
            0,
            0,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            0,
            1,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            0,
            2,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            0,
            3,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            1,
            0,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            1,
            1,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            1,
            2,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            1,
            3,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_metal_1",
        ),
        (
            2,
            0,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            2,
            1,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            2,
            2,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            2,
            3,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_air_plant",
        ),
        (
            3,
            0,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            3,
            1,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            3,
            2,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            3,
            3,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_tanks",
        ),
        (
            4,
            0,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            4,
            1,
            "basic_oxygen_furnace_tile_2",
            "basic_oxygen_furnace_spritelayout_animated_ladle_rear_part",
        ),
        (
            4,
            2,
            "basic_oxygen_furnace_tile_2",
            "basic_oxygen_furnace_spritelayout_animated_ladle_front_part",
        ),
        (
            4,
            3,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_small_shed",
        ),
    ],
)
industry.add_industry_layout(
    id="basic_oxygen_furnace_industry_layout_4",
    layout=[
        (
            0,
            0,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            0,
            1,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            0,
            2,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            1,
            0,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            1,
            1,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            1,
            2,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            2,
            0,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            2,
            1,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            2,
            2,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_air_plant",
        ),
        (
            3,
            0,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            3,
            1,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            3,
            2,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_tanks",
        ),
        (
            4,
            0,
            "basic_oxygen_furnace_tile_2",
            "basic_oxygen_furnace_spritelayout_animated_ladle_rear_part",
        ),
        (
            4,
            1,
            "basic_oxygen_furnace_tile_2",
            "basic_oxygen_furnace_spritelayout_animated_ladle_front_part",
        ),
        (
            4,
            2,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_small_shed",
        ),
    ],
)
industry.add_industry_layout(
    id="basic_oxygen_furnace_industry_layout_5",
    layout=[
        (
            0,
            0,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            0,
            1,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            0,
            2,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            0,
            3,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_air_plant",
        ),
        (
            1,
            0,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            1,
            1,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            1,
            2,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            1,
            3,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_tanks",
        ),
        (
            2,
            0,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            2,
            1,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            2,
            2,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_furnace",
        ),
        (
            2,
            3,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            3,
            0,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_casting_shed",
        ),
        (
            3,
            1,
            "basic_oxygen_furnace_tile_2",
            "basic_oxygen_furnace_spritelayout_animated_ladle_rear_part",
        ),
        (
            3,
            2,
            "basic_oxygen_furnace_tile_2",
            "basic_oxygen_furnace_spritelayout_animated_ladle_front_part",
        ),
        (
            3,
            3,
            "basic_oxygen_furnace_tile_1",
            "basic_oxygen_furnace_spritelayout_small_shed",
        ),
    ],
)
