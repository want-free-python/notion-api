## 회고

#### 처음 들어본 브레드크럼스

처음 노션 API 팀 과제를 받았을 때, 다른 게시물 API 만드는 것처럼 쉽게 만들면 되겠지라고 생각했다. 그렇게 과제 설명을 듣고 있는데, 처음 보는 용어가 나왔다.

**"브레드크럼스"**

뭐냐...? 과제 이야기도 들으며 찾아보았는데, 헨젤과 그레텔의 빵부스러기를 본 따 만들어진 페이지 뎁스 기록을 말하는 거였다. 실제로 많이 쓰던 기능의 이름이 저런 이름인지 처음 알았고, 새로운 용어를 배워서 그런가? 과제 설명이 끝나기도 전에 구현방법에 대해 상상했다. 다른 기능들이야 별 어려움이 없을 것 같았고, 브레드크럼스 이 녀석이 주된 과제의 목표였다.

<br/>

#### 어떻게 구현해야 할까?

 처음 브레드크럼스를 생각했을 땐, 무식하게 부모 페이지를 찾아나가는 거 였다. 당연히 O(n)의 시간이 걸리는 작업이고 이는 DB 커넥션 비용도 있기 때문에 가볍게 무시할 수 있는 부분이 아니었다. 그래서 생각한게 대략적으로 캐싱하는 방법이었다. 페이지를 쓸 때 무효화하는 방법을 택하여 캐싱한 데이터를 불러올 수 있다면 그만한 속도를 다른 로직에서 못 낼거라 생각했기 때문이다. 그렇게 캐싱을 염두에 두고 1차 회의를 시작했다.

<br/>

#### 시간에 맞춰 구현하다

 1차 회의를 하면서 다들 생각해온 것과 팀 과제의 방향을 설정하기 시작했고 시간낭비도 좀 있었지만 결국은 서로의 생각을 다 공유하고 인사이트를 얻으며 각자 코드를 준비할 수 있는 기반을 가지게 되었다. 그후, 회의를 통해 얻은 지식으로 각자 코드를 짜서 PR 올리기로 했고 머리 속으로 구현하기 쉬운 로직부터 구현하기 시작했다. (갈의 법칙을 믿는 편이라 빠르게 동작할 수 있게 만들고 싶었다.) 무작정 부모 페이지를 찾아가는 방식을 구현하였고, Raw SQL로 보내고 프레임워크의 편리성을 이용 못하니 생산성이 떨어져 생각보다 시간이 많이 걸렸다. 그래서 캐싱처럼 구현하는 방식을 우리끼리의 제한시간 내에 못 할 수도 있겠다고 생각했다. 하지만 생각해보니 내가 바꿀건 브레드크럼스 로직 밖에 없었다. 그게 제일 큰 로직이긴 하지만 그래도 이것만 바꾸면 된다고 생각하니 할만하다 느꼈다. 차근차근 머리에 정리해놓은 로직을 꺼내놓았고, 구현하다보니 그 로직들이 죽도록 풀었던 DP, BFS 알고리즘이었다. 그렇게 캐싱구조처럼 브레드크럼스를 빨리 가져오는 로직을 완성할 수 있었고 팀원들에게 보여줄 수 있었다.

<br/>

#### 역시 재밌는 문제해결

 처음 해본 브레드크럼스 구현이라 재밌기도 하고 실제 이런 기능이 필요한 서비스를 만드는 개발자들에 대한 부러움도 느꼈다. (왜냐면 실무할 때, B2B 서비스를 만들었고 브레드크럼스 같은 사용자편리성에 대한 내용보다는 기능중점 서비스였기 때문 ㅠㅠ) 이젠 이직할거니 이런 것도 써볼 수 있는 회사를 다닐 수도 있겠다는 생각을 한다.

 마지막으로 이번 팀 과제를 통해 팀원들과 문제해결하는 과정을 같이 느낄 수 있어 좋았고, 다음 과제도 있으면 기간이 좀 길어서 다 같이 더 고민해볼 수 있었으면 좋겠다는 생각을 했다.