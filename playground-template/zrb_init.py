from zrb import CmdTask, StrInput, runner

cmd_template = '''
for i in 1 2 3 4 5
do
    echo "{word} $i"
done
'''

ding = CmdTask(
    name='ding',
    inputs=[
        StrInput(name='satu', shortcut='s', default='1', prompt='satu'),
        StrInput(name='dua', shortcut='d', default='2', prompt='dua'),
    ],
    cmd=cmd_template.format(word='ding')
)

dong = CmdTask(
    name='dong',
    inputs=[
        StrInput(name='tiga', shortcut='t', default='3', prompt='tiga'),
        StrInput(name='empat', shortcut='e', default='4', prompt='empat'),
    ],
    cmd=cmd_template.format(word='dong')
)

dingdong = CmdTask(
    upstreams=[ding, dong],
    cmd=cmd_template.format(word='ding dong')
)

runner.register(ding)
runner.register(dong)
runner.register(dingdong)