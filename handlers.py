from models import Condition, choose_condition


def handle_continue(user, call, bot):
    user.condition = Condition.get_by_id(2)
    user.save()
    current_condition = choose_condition(user.condition.id)(bot)
    current_condition.proceed_commands(call.message)


def handle_section_1(user, call, bot):
    user.condition = Condition.get_by_id(3)
    user.save()
    current_condition = choose_condition(user.condition.id)(bot)
    current_condition.proceed_section_1(call.message)


def handle_section_2(user, call, bot):
    user.condition = Condition.get_by_id(3)
    user.save()
    current_condition = choose_condition(user.condition.id)(bot)
    current_condition.proceed_section_2(call.message)


def handle_section_3(user, call, bot):
    user.condition = Condition.get_by_id(3)
    user.save()
    current_condition = choose_condition(user.condition.id)(bot)
    current_condition.proceed_section_3(call.message)


def handle_section_4(user, call, bot):
    user.condition = Condition.get_by_id(3)
    user.save()
    current_condition = choose_condition(user.condition.id)(bot)
    current_condition.proceed_section_4(call.message)


def handle_goods_1(user, call, bot):
    user.condition = Condition.get_by_id(4)
    user.save()
    current_condition = choose_condition(user.condition.id)(bot)
    current_condition.proceed_goods_1(call.message)


def handle_goods_2(user, call, bot):
    user.condition = Condition.get_by_id(4)
    user.save()
    current_condition = choose_condition(user.condition.id)(bot)
    current_condition.proceed_goods_2(call.message)


def handle_goods_3(user, call, bot):
    user.condition = Condition.get_by_id(4)
    user.save()
    current_condition = choose_condition(user.condition.id)(bot)
    current_condition.proceed_goods_3(call.message)


def handle_goods_4(user, call, bot):
    user.condition = Condition.get_by_id(4)
    user.save()
    current_condition = choose_condition(user.condition.id)(bot)
    current_condition.proceed_goods_4(call.message)


def handle_goods_5(user, call, bot):
    user.condition = Condition.get_by_id(4)
    user.save()
    current_condition = choose_condition(user.condition.id)(bot)
    current_condition.proceed_goods_5(call.message)


def handle_goods_6(user, call, bot):
    user.condition = Condition.get_by_id(4)
    user.save()
    current_condition = choose_condition(user.condition.id)(bot)
    current_condition.proceed_goods_6(call.message)


def handle_goods_7(user, call, bot):
    user.condition = Condition.get_by_id(4)
    user.save()
    current_condition = choose_condition(user.condition.id)(bot)
    current_condition.proceed_goods_7(call.message)


def handle_goods_8(user, call, bot):
    user.condition = Condition.get_by_id(4)
    user.save()
    current_condition = choose_condition(user.condition.id)(bot)
    current_condition.proceed_goods_8(call.message)


def handle_goods_9(user, call, bot):
    user.condition = Condition.get_by_id(4)
    user.save()
    current_condition = choose_condition(user.condition.id)(bot)
    current_condition.proceed_goods_9(call.message)


def handle_goods_10(user, call, bot):
    user.condition = Condition.get_by_id(4)
    user.save()
    current_condition = choose_condition(user.condition.id)(bot)
    current_condition.proceed_goods_10(call.message)


def handle_goods_11(user, call, bot):
    user.condition = Condition.get_by_id(4)
    user.save()
    current_condition = choose_condition(user.condition.id)(bot)
    current_condition.proceed_goods_11(call.message)


def handle_goods_12(user, call, bot):
    user.condition = Condition.get_by_id(4)
    user.save()
    current_condition = choose_condition(user.condition.id)(bot)
    current_condition.proceed_goods_12(call.message)


def handle_backwards(user, call, bot):
    user.condition = Condition.get_by_id(user.condition.id - 1)
    user.save()
    current_condition = choose_condition(user.condition.id)(bot)
    current_condition.proceed_commands(call.message)


def handle_backwards_croissant(user, call, bot):
    user.condition = Condition.get_by_id(user.condition.id - 1)
    user.save()
    current_condition = choose_condition(user.condition.id)(bot)
    current_condition.proceed_section_1(call.message)


def handle_backwards_pie(user, call, bot):
    user.condition = Condition.get_by_id(user.condition.id - 1)
    user.save()
    current_condition = choose_condition(user.condition.id)(bot)
    current_condition.proceed_section_2(call.message)


def handle_backwards_pancake(user, call, bot):
    user.condition = Condition.get_by_id(user.condition.id - 1)
    user.save()
    current_condition = choose_condition(user.condition.id)(bot)
    current_condition.proceed_section_3(call.message)


def handle_backwards_cake(user, call, bot):
    user.condition = Condition.get_by_id(user.condition.id - 1)
    user.save()
    current_condition = choose_condition(user.condition.id)(bot)
    current_condition.proceed_section_4(call.message)
