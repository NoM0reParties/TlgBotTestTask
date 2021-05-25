import models
from bot_conditions import choose_condition


def backwards_processor(call):
    parsed_data = call.data.split('_')
    model_name = parsed_data[-2].title() + 'Model'
    get_model = getattr(models, model_name)
    return get_model.get_by_id(int(parsed_data[-1]))


def handle_showcase(user, call, bot):
    user.condition = models.Condition.get_by_id(2)
    user.save()
    id_key = int(call.data.split('_')[-1])
    model = models.ShowcaseModel.get_by_id(id_key)
    current_condition = choose_condition(user.condition.id)(bot)
    current_condition.proceed_commands(call.message, model)


def handle_section(user, call, bot):
    user.condition = models.Condition.get_by_id(3)
    user.save()
    id_key = int(call.data.split('_')[-1])
    model = models.SectionModel.get_by_id(id_key)
    current_condition = choose_condition(user.condition.id)(bot)
    current_condition.proceed_commands(call.message, model)


def handle_goods(user, call, bot):
    user.condition = models.Condition.get_by_id(4)
    user.save()
    id_key = int(call.data.split('_')[-1])
    model = models.GoodsModel.get_by_id(id_key)
    current_condition = choose_condition(user.condition.id)(bot)
    current_condition.proceed_commands(call.message, model)


def handle_backwards(user, call, bot):
    user.condition = models.Condition.get_by_id(user.condition.id - 1)
    user.save()
    model = backwards_processor(call)
    current_condition = choose_condition(user.condition.id)(bot)
    current_condition.proceed_commands(call.message, model)
