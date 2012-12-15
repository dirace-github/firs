from firs import Cargo

cargo = Cargo(id = 'sugar_beet',
              number = '12',
              type_name = 'string(STR_CARGO_NAME_SUGAR_BEET)',
              unit_name = 'string(STR_CARGO_NAME_SUGAR_BEET)',
              type_abbreviation = 'string(STR_CID_SUGAR_BEET)',
              sprite = 'NEW_CARGO_SPRITE',
              weight = '1.0',
              station_list_colour = '182',
              cargo_payment_list_colour = '182',
              is_freight = '1',
              cargo_classes = 'bitmask(CC_BULK)',
              cargo_label = '"SGBT"',
              town_growth_effect = 'TOWNGROWTH_NONE',
              town_growth_multiplier = '1.0',
              units_of_cargo = '80',
              items_of_cargo = 'string(STR_CARGO_UNIT_SUGAR_BEET)',
              penalty_lowerbound = '5',
              single_penalty_length = '30',
              price_factor = '116.194725037',
              disabled_climates = ['CLIMATE_TROPICAL'])

cargo.economy_variations['BASIC']['disabled'] = True
