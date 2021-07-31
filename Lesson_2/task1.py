from string import Template

name = 'Oleksandr'
current_day = 'Saturday'

print('Good day '+name+'! '+current_day+' is a perfect day to learn some python.')
print(f'Good day {name}! {current_day} is a perfect day to learn some python.')
print('Good day {}! {} is a perfect day to learn some python.'.format(name, current_day))
print('Good day {1}! {0} is a perfect day to learn some python.'.format(current_day, name))
print('Good day %s! %s is a perfect day to learn some python.' % (name, current_day))
print(Template('Good day $name! $current_day is a perfect day to learn some python.')
      .substitute(name=name, current_day=current_day))

