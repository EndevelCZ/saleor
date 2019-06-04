![github_saleor_readmew_header_01](https://user-images.githubusercontent.com/5421321/47800694-19bec680-dd2d-11e8-8625-2ed7c690bc13.jpg)

<div align="center">
  <h1>Saleor</h1>
</div>

<div align="center">
  <strong>E-commerce for the PWA era</strong>
</div>

<div align="center">
  A modular, high performance e-commerce storefront built with GraphQL, Django, and ReactJS.
</div>

<br>

<div align="center">
  Join our active, engaged community: <br>
  <a href="https://getsaleor.com/">Website</a>
  <span> | </span>
  <a href="https://medium.com/saleor">Blog</a>
  <span> | </span>
  <a href="https://twitter.com/getsaleor">Twitter</a>
  <span> | </span>
  <a href="https://gitter.im/mirumee/saleor">Gitter</a>
  <span> | </span>
  <a href="https://spectrum.chat/saleor">Spectrum</a>
</div>

<br>

<div align="center">
  <a href="https://circleci.com/gh/mirumee/saleor">
    <img src="https://circleci.com/gh/mirumee/saleor.svg?style=svg" alt="Build status" />
  </a>
  <a href="http://codecov.io/github/mirumee/saleor?branch=master">
    <img src="http://codecov.io/github/mirumee/saleor/coverage.svg?branch=master" alt="Codecov" />
  </a>
  <a href="https://docs.getsaleor.com/en/latest/?badge=latest">
    <img src="https://readthedocs.org/projects/saleor/badge/?version=latest" alt="Documentation Status" />
  </a>
  <a href="https://github.com/python/black">
    <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black">
  </a>
</div>


## Table of Contents
- [What makes Saleor special?](#what-makes-saleor-special)
- [Features](#features)
- [Installation](#installation)
- [Demo](#demo)
- [Contributing](#contributing)
- [Translations](#translations)
- [Your feedback](#your-feedback)
- [License](#license)


## What makes Saleor special?

Saleor is a rapidly-growing open source e-commerce platform that has served high-volume companies from branches like publishing and apparel since 2012. Based on Python and Django, the latest major update introduces a modular front end powered by a GraphQL API and written with React and TypeScript.

## Features
- __PWA__: End users can shop offline for better sales and shopping experiences
- __GraphQL API__: Access all data from any web or mobile client using the latest technology
- __Headless commerce__: Build mobile apps, customize storefronts and externalize processes
- __UX and UI__: Designed for a user experience that rivals even the top commercial platforms
- __Dashboard__: Administrators have total control of users, processes and products
- __Orders__: A comprehensive system for orders, dispatch and refunds
- __Cart__: Advanced payment and tax options, with full control over discounts and promotions
- __Payments__: Flexible API architecture allows integration of any payment method. Comes with Braintree support out of the box.
- __Geo-adaptive__: Automatic localized pricing. Over 20 local languages. Localized checkout experience by country.
- __SEO__: Packed with features that get stores to a wider audience
- __Cloud__: Optimized for deployments using Docker
- __Analytics__: Server-side Google Analytics to report e-commerce metrics without affecting privacy

Saleor is free and always will be.
Help us out… If you love free stuff and great software, give us a star! 🌟

![1 copy 2x](https://user-images.githubusercontent.com/5421321/47798207-30aeea00-dd28-11e8-9398-3d8426836a83.png)
![group 2 2x](https://user-images.githubusercontent.com/5421321/47799917-8afd7a00-dd2b-11e8-88c7-63588e25bcea.png)


## Installation

Saleor requires Python 3.6+, Node.js 10.0+, PostgreSQL and OS-specific dependency tools.

[See the Saleor docs](https://saleor.readthedocs.io) for step-by-step installation and deployment instructions.


## Demo

Want to see Saleor in action?

[View Storefront](http://demo.getsaleor.com/) | [View Dashboard (admin area)](http://demo.getsaleor.com/dashboard/)

Or launch the demo on a free Heroku instance.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Login credentials: `admin@example.com`/`admin`


## PWA Storefront
The PWA, single-page storefront lives in a [separate repository](https://github.com/mirumee/saleor-storefront).

[View PWA Storefront](https://pwa.getsaleor.com/)


## Contributing
We love your contributions and do our best to provide you with mentorship and support. If you are looking for an issue to tackle, take a look at issues labelled [`Help Wanted`](https://github.com/mirumee/saleor/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22).

If nothing grabs your attention, check [our roadmap](https://github.com/mirumee/saleor/projects/6) or come up with your own feature. Just drop us a line or [open an issue](https://github.com/mirumee/saleor/issues/new) and we’ll work out how to handle it.

Get more details in our [Contributing Guide](https://saleor.readthedocs.io/en/latest/contributing.html).


## Translations

Did you know that Saleor is available in almost 30 languages, translated entirely by our community?

If you'd like to help us, you can join one of our translation teams on [the localization platform Transifex](https://www.transifex.com/mirumee/saleor-1/languages/).

The repository gets synchronized weekly with the latest contributions.


## Your feedback

Do you use Saleor as an e-commerce platform?
Fill out this short survey and help us grow. It will take just a minute, but mean a lot!

[Take a survey](https://mirumee.typeform.com/to/sOIJbJ)


## License

Disclaimer: Everything you see here is open and free to use as long as you comply with the [license](https://github.com/mirumee/saleor/blob/master/LICENSE). There are no hidden charges. We promise to do our best to fix bugs and improve the code.

Some situations do call for extra code; we can cover exotic use cases or build you a custom e-commerce appliance.


#### Crafted with ❤️ by [Mirumee Software](http://mirumee.com)
hello@mirumee.com


## Endevel CZ part follows

###Instalation according to [docs](https://saleor.readthedocs.io/en/latest/gettingstarted/installation-linux.html)

globální debian/ubuntu balíčky
```
sudo apt-get install build-essential python3-dev python3-pip python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info
```

naklonovat repository
```
git clone https://github.com/mirumee/saleor.git
cd saleor
```
případně překopírovat vešketerý obsah (kromě `.git`) do složky nového projektu

vytvořit virtualenv a nainstalovat závisloti
```
virtuaelenv .venv --python=/usr/bin/python3
pip install -r requirements.txt
```

příklad pro user saleor s helsem saleor, db saleor
```
CREATE USER saleor WITH PASSWORD 'saleor';
CREATE DATABASE saleor OWNER saleor;
GRANT CONNECT ON DATABASE saleor TO saleor;
\c saleor;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO saleor;
```

připravit databázi - musí odpovídat settingům v common.env

```.env
DATABASE_URL=postgres://matpro_eshop:matpro_eshop@localhost/matpro_eshop
```

#### DB setting TODO 
1) Migrace vytváří extensions, takže db user musí být superuser `ALTER USER matpro_eshop WITH SUPERUSER;` 
(v dokumentaci radí mít jednoho usera pouze pro migraca)
2) Přijít na to, jak propagovat setting databáze (prozatím přepsán default v base.py)
 
nastavit secret key jako ENV proměnnou (TODO předělat)
```
 export SECRET_KEY='<mysecretkey>'
``` 

udělat db (default name je saleor, pass saleor, user saleor) a zmigrovat    
TODO podle dokumetnace může vyžadovat nějaké DB EXTENSIONS, ale zatím jsem 
si to neověřil
```
python manage.py migrate
```

front 
```
npm install
npm run build-assets
npm run build-emails 
```

nejspíš budeme chtít ještě
```
python manage.py createsuperuser
```

a můžeme jet
```
python manage.py runserver
```

### Vývoj
Django pouštíme klasicky, pomocí `npm start` pustíme webpack watcher pro
SCSS a JS soubory, takže je nemusíme updatovat (build trvá několik vteřin)

#### Zisk updatů z hlavního upstreamu

Merge upstreamu originálího repo (dělá se v repo EndevelCZ/saleor)

```
git pull https://github.com/mirumee/saleor master
```

Pokud selže na konfliktu, otevřeme v Pycharmu záložku `9: Version Control` 
a vyřešíme konflikty klasicky a následně commitneme merge a pushneme k nám.

#### Zisk updatů v jednotlivých eshopech

Každý eshop musí být vytvořený následujícím způsobem

Nejdříve vytvoříme nový repozitář (bez README.md) - tzn. naprosto prázdný


```
git clone git@bitbucket.org:endevel/NEWSHOP_saleor.git  
git remote add sync git@github.com:endevelcz/saleor.git # popr. mirumee/saleor.git
git remote -v                                           # zkontrolovat
git pull sync master                                    # pullneme sync upstream
git branch --track github sync/master                   # nastavíme github branch pro sync
git push -u origin master                               # pushenme všechno do masteru     

```
 
Pak už "jenom" pravidelně pullujeme v `github` větvi a mergujeme jí do masteru

**NIKDY NEPUSHUJEME DO `github` větve, protože ta se updatuje přes `endevelcz/saleor` 
github repo**

#### Old version of getting updates

Merge upstreamu originálího repo (dělá se v repo EndevelCZ/saleor)

```
git pull https://github.com/mirumee/saleor master
```

Pokud selže na conflictu, otevřeme v Pycharmu záložku `9: Version Control` 
a vyřešíme conflicty klasicky a následně commitneme merge a pushneme k nám.

Po otestování změn na ukázkovém eshopu běžící přímo z EndevelCZ/saleor repa 
můžeme přenést změny i do eshopu

1) uděláme a checknoutneme větev `update`
2) ručně přeneseme soubory (třeba všechny najednou)
3) commitneme a pushneme
4) uděláme merge do masteru našeho eshopu (zahodíme, co nechceme přepsat)

TOOD vymyslet něco lepšího
