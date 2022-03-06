import re

liczby = "Dzisiaj mamy 4 stopnie na plusie, 1 marca 2022 roku"
print(re.sub('\d', '', liczby))
znaki_html = "<div><h2>Header</h2> <p>article<b>strong text</b> <a href="">link</a></p></div>"
print(re.sub('<[^>]*>', '', znaki_html))
znaki_interpunkcyjne = "Lorem ipsum dolor sit amet, consectetur; adipiscing elit. Sed eget mattis sem. Mauris egestas erat quam, ut faucibus eros congue et. In blandit, mi eu porta; lobortis, tortor nisl facilisis leo, at tristique augue risus eu risus."
print(re.sub('[.,;]', '', znaki_interpunkcyjne))
hashtagi = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed #texting eget mattis sem. Mauris #frasista egestas erat #tweetext quam, ut faucibus eros #frasier congue et. In blandit, mi eu porta lobortis, tortor nisl facilisis leo, at tristique #frasistas augue risus eu risus."
print(re.findall('#[\w]+', hashtagi))
emotikony = "Lorem ipsum dolor :) sit amet, consectetur; adipiscing elit. Sed eget mattis sem. ;) Mauris ;( egestas erat quam, :< ut faucibus eros congue :> et. In blandit, mi eu porta; lobortis, tortor :-) nisl facilisis leo, at ;< tristique augue risus eu risus ;-)."
print(re.findall('[:;][^\s]+', emotikony))


